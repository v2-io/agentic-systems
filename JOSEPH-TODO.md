# JOSEPH-TODO — decisions routed to Joseph

> [!note]
> **What this is.** The *short* list of open items that genuinely need *Joseph's* decision or taste — ones an agent should not just default. Pointers, not duplicated context. **Work items live in their home trackers** (`TODO.md` / `PROPOSALS.md` / `INTEGRATION-CLEANUP-TODO.md`); a decision-*point* alone does not make something Joseph's — most have a sensible default the lead takes and proceeds on.
>
> **Convention (for agents):** add an entry here *only* when the call is genuinely Joseph's — **irreversible**, **publication/authoring-voice**, **cross-project blast-radius**, or **"did this actually come from Joseph?"**. Otherwise default-and-proceed (note it under "lead will handle" if it's a close call). Remove an entry when decided.

## Needs your decision (genuinely only-you)

**→ [`msc/decision-briefs-2026-07-15.md`](msc/decision-briefs-2026-07-15.md) — the open Joseph-decisions as one-sitting briefs** (each verified against current state 2026-07-15; ordered quick-nods → policy → theory/naming → strategic; each carries context + options + lead-rec + pointer, decidable from the brief alone). The queue, one line each:

*Time-bound:* FAST @ NeurIPS 2026 (Foundations of Agentic Systems Theory workshop) deadline **2026-08-29** — the survey found it is the one venue named around "agentic systems theory"; submit-or-not is yours (`ref/prior-art-analysis/agentic-systems-landscape-2026-08-22.md`).

*Quick nods:* F72 external-eye release · (PI) used-before-introduced — `#der-gain-sector-bridge` consumes `#scope-agent-identity` without listing it in `depends:`; hoist / add dep / reorder is a placement call (731548/35) · `core.hooksPath` unset (still set to the dead pre-rename path as of 2026-08-22) · `.claude/` selective un-gitignore · `.archive/` untracking (the fonts half landed 2026-07-15). *(Decided by action since the briefs were written: CURRENT-VOL1 — made a generated reader snapshot 2026-08-22; Zenodo — v0.4.0 version DOI minted 2026-08-15.)*
*Policy:* gold-dir standing gate (largest unblock: 0/22 graduated) · promotion-terminus / WN drain (sharpened by your 2026-07-14 stage position) · CLAUDE.md generate+cadence · naming-vs-Findings de-block.
*Theory & naming:* SP-30 typed epistemic target (package ready) · C5 intelligence-empathy landing · the 01 ordering structural call + 9 whitelist-or-reorder rows · separability-triad rung names · agent-spectrum tetrad · Greek-vocabulary per-term · LEXICON §F reorg.
*Strategic:* 04-eli-core own/private repo (new fact: repo already public).

## From the 2026-08-22 cleanup pass (only-you)

- **Five `missing` Vol-3 segments** (`obs-backward-inference-empathy`, `form-structured-rich-context`, `der-active-salience-management`, `der-self-referential-closure`, `def-cognitive-fusion`): write at honest tier, or recast the three `03-llm-core/src/impl-*` passages that describe them in the present tense ("carries", "defines", "addresses") as anticipated. Forward refs per se are sanctioned by FORMAT; the present-tense content claims are the defect.
- **Nine scope-first OUTLINE orderings in 03/04** — whitelist (`OUTLINE-accepted.md`, mechanism proven in 01) if deliberate, else reorder. (Also in the valve.)
- **GitHub v0.4.0 release body** still says the root CURRENT-VOL1 files are byte-identical to the assets — `gh release edit v0.4.0 --notes-file releases/v0.4.0.md` would sync it.
- **Corpus press.** Every tracker, `CHANGELOG.md`, and several segments fail `md-press --check` at HEAD (pre-existing wrap debt). Pressing them in place is mechanical once the two md-press bugs filed 2026-08-22 (`firmatum/utils/md-press/FEEDBACK-2026-08-22.md`: pseudo-display `$$` join; missing GitHub math-compat checks) are fixed — your call whether to press before or after.

## Small, outside-repo, only-you (migrated from the drained NEXT-UP, 2026-06-02 vintage)

- Commit the global `~/.claude/CLAUDE.md` — your in-progress edits are mixed with the 2026-06-02 condensation; `~/.claude/CLAUDE.md.bak` marks the boundary. (Optional companion: eyeball the `MEMORY.md` trims from the same pass.)

## Lead will default-and-proceed (flag only if you'd rather weigh in)

- **`#schema-strategy-persistence` hard-ceiling** → take adjudication verdict B as settled (name the convention, keep `status: exact`).
- **SP-27 / SP-29** (Part-I↔Part-IV bridge placement; the infrastructure-as-active-monitor meta-segment candidate) → lead/architectural judgment, tracked in [`PROPOSALS.md`](PROPOSALS.md).
- **Greek-vocabulary prose discipline** (tighten segment prose vs soften the README claim, per term) → lead per-term pass, in [`TODO.md`](TODO.md).

*(Pure work — the global `~/.claude/` SOP pass, the TODO-freshness pass incl. the NeurIPS-section reframe and `domain-xfer-candidates` modernization, the README-v2 pass — is not a decision and is not listed here; it lives in `TODO.md` / its home trackers.)*
