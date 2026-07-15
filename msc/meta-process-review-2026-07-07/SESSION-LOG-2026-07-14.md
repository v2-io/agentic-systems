# Session log — 2026-07-14 (Archema catch-up, autonomous)

*Joseph away; mandate: "update any Archema stuff you can with reasonable confidence… low risk since none of it is ratified." Everything here is uncommitted working-tree state for your review. Nothing ratified, nothing committed.*

## What I changed (confident, low-risk — dead pointers + stale names)

The reorg's program docs (2026-07-09/10) predate vivarium's ETHICS reorg (07-11→13), so they carry dead `ASF.md` pointers. Verified the moratorium's new home first-hand (`vivarium/ETHICS.md` "Standing Moratorium Imperative"; `ASF.md` gone; confirmed by vivarium's own `DECISIONS.decision-log.udon:894`). Repointed **only the moratorium references** — I did **not** guess a target for the homeless non-§0 content (see ledger).

- `CHARTER-DRAFT.md` — register table (§0 members: `agentic-systems`→`asf`, `synthese-paper`→`logos`; `ASF.md (incl §0)`→`ETHICS.md`), §3 line 40, §4 line 46, §10 Level-B line 86 → all moratorium refs now `ETHICS.md`.
- `CLAUDE.md` (program) — moratorium ref → `ETHICS.md`; the "vivarium requires its ASF.md every session" line rewritten to the true current state (ETHICS.md front-door + Level-C gate; the rest re-homing → ledger).
- `charter/concept-matrix.md` — the moratorium row (§81) → `ETHICS.md`. **Left untouched:** the §2-handshake cell (row 13) and the §7.5-*in-vivia* cell (row 82) — their content is homeless-in-archive; guessing a live target would be worse than a tracked-stale ref. Both are in the ledger.
- `README.md` — member names `agentic-systems`/`synthese-paper` → `asf`/`logos` (with "formerly"/remote notes matching CLAUDE.md).
- `asf/doc/sop/agents.sop.md` (= asf `CLAUDE.md`) — the vivarium-bridge line's dead `ASF.md` → `ETHICS.md` + dissolution note.

## What I created

- **`charter/INCOHERENCE.md`** — the incoherence ledger charter §8 says to "create on first entry." First entry is the verified homeless-ASF.md-content divergence (row 1); rows 2–4 are the charter's own §8 seeds, carried but marked *not re-verified this session*. Plus a standing note that vivarium is mid-rebuild = a known volatile divergence zone.
- **`vivarium/feedback-from-asf.md`** — short asf-perspective note for the vivarium rebuild (per your suggestion): which homeless content the program/asf docs depend on, so re-homing can prioritize.

## What I deliberately did NOT do (and why)

- **No guessing homeless targets** — §2/§7.5/Level-C content is in `.archive/ASF.md` awaiting re-homing; tracked, not patched.
- **No charter restructure** — I still think the charter restates substantive theory that could be cited-not-restated (the G1 amplifier risk), but that's a design judgment for your ratification pass, not a reasonable-confidence catch-up edit. Flagged, not executed.
- **No vivarium internals** — it's mid-teardown; I left a note instead.
- **No asf-local backlog work** — the census items (gold-dir gate, bulk-64, promotion terminus, WN deluge) stay queued per your "asf-specific work queued" steer.
- **No pre-existing lint sweep** — `charter/concept-matrix.md` (bare Greek in ~30 table cells) and `README.md` (hard-wrapped prose) carry lint debt that predates this session; a sweep is its own task (and the concept-matrix's dense Greek cells carry table-mangling risk). My new/edited files are lint-clean; the moratorium refs are fully repointed.

---

## Proposal: consolidating memory for launch-from-root

*You asked for ideas on consolidating memories so you can launch from `archema-io/` root. Here's the shape; the migration itself is your call (cross-project blast radius).*

**The mechanics that constrain it:** project memory loads by **exact session-start dir only** and does **not** cascade. So:
- **Global** (`~/.claude/CLAUDE.md` + `~/.claude/memory/`) loads in *every* session, root or member. It already carries the universal disposition + user context + the global reader-model.
- **Program** memory (`-archema-io`) loads only at root; **member** memory only in that member. Neither cascades to the other.

**The dedup opportunity (the real find):** many `asf` project-memory `feedback_*` files are *program-wide disciplines* — the charter §2 explicitly codifies the disposition as program-wide — and several already exist in global too. That's triplication waiting to happen (global + asf + a would-be program copy). One referent wants one canonical home.

**Recommended layering:**
1. **Universal disciplines → canonical in GLOBAL.** Anything project-agnostic (strengthen-before-soften, integration-is-replacement, peer-voice, durability-by-tool-action, voice-discipline, superlatives, efficiency-is-the-tell, primary-source, math-novelty-recognition, …) belongs in global, which loads everywhere. Audit the three member memories; lift the project-agnostic ones to a single global home and dedup the copies. **Result: root-launch and member-launch both always get the disposition.**
2. **Program-scoped procedural → PROGRAM memory** (already thin and correct): the memory-routing rule, superlatives, efficiency-tell, the Archema-structure orientation. Keep.
3. **Member-local → stays member-local:** asf's FORMAT/lint/naming/audit specifics; vivarium's determinism/probes/udon-subset; logos' venue registers.
4. **The root-launch experience then:** global (universal) + program (orientation/procedural) give a strong baseline at root. Member-specific disciplines still need the explicit member-index Read the CLAUDE bridge prompts. To kill that friction later: a `SessionStart`/first-file-touch **hook** that detects which member dir the work touches and surfaces its index — but that's harness tooling (its own small task), not a memory move.

**The one action to decide:** a deliberate audit pass that classifies every project-memory file as *universal / program / member*, lifts the universal ones to a global canonical home, and dedups. Cross-project blast radius → your call and a deliberate pass, not a drive-by. I can draft the classification (a table of every current memory file → proposed home) whenever you want it — that's the low-risk next step that makes the decision concrete without moving anything.
