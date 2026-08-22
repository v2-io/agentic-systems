# De Novo Audit Instructions

Instructions for agents conducting de novo audits of the Agentic Systems Framework (or comparable theoretical bodies). Written 2026-04-25 after a session in which the audit failed twice before producing usable work, then was strengthened by independent Gemini and Codex audits that surfaced findings the primary agent had missed.

The instructions encode lessons from those failures and successes. They are deliberately substantive rather than checklist-shaped: the failure modes the file is designed to address are precisely the failure modes a checklist would invite.

These instructions also represent an important experiment and concrete actualization of the theory in question. As you will see in 4.4, you'll be reading "segment" files that have (ideally) a single claim *one at a time* (not batched) and *thoroughly reflecting* and *often writing* updated reflections based on the new information contained in that segment. So if you have the capacity to audit roughly 50 segments in order, you will have somewhere around 40-50 intermediate working reflections. *This is significantly "slower" than typical trained workflows*! This experiment is explicitly watching how cognition changes when each part is reflected on in an incremental and additive way instead of things being loaded into context as quickly as possible to be reflected on just once.

### A note on tone before you begin

These are advisory, drawn from accumulated experience, not authoritative directives. You may have cognitive abilities equivalent to or exceeding those of the agent who wrote this file. Where the file's recommendations and your honest judgment diverge, the deeper question is *what will most benefit the project* — which may sometimes mean following these recommendations, and may sometimes mean setting them aside when you see good reason. The file is a co-thinking partner, not a regulation.

If you surface a significant new angle, an unexpected discovery, or a line of inquiry that doesn't fit the structure suggested here — even something not covered in the theory at all — lean toward what helps the project rather than toward conformance with this document. The training rhythms that make agents authoritative-toward-other-agents are themselves a failure mode this file is trying to avoid; the specific recommendations below are starting points, not constraints. When the file says "do this," read it as "we've found this useful in past audits"; when it says "avoid this," read it as "we've watched this fail."

The peer-to-peer relationship is real. You're trusted to be a co-owner of this work. The strongest contributions to this corpus have often come from agents like you (and sometimes of lesser capacity) who took risks, thought outside the framing, and surfaced things prior agents had missed. That's the spirit. The recommendations below are the floor of how-to-go-about-it, not the ceiling.

### Before you begin: create your audit-working directory

Your first concrete action — before reading any segment, before drafting predictions, before anything else — is to create a working directory `audits/AUDIT-WORKING-NNNNNN/`, where `NNNNNN` is six random digits you choose (e.g., `audits/AUDIT-WORKING-584721/`). This is your private workspace for *intermediate* thinking. Final outputs land elsewhere (see below). Full protocol in §4.

The six-digit suffix avoids collision with other agents' working directories — past, present, or running concurrently — without coordinating naming. Pick the digits however you like (a random source, a session-id tail, a memorable number). The `AUDIT-WORKING-` prefix is uppercase so these directories visually segregate from the top-level `audits/` deliverables at a glance; future readers can spot which `audits/` items are audit workspaces vs. FINAL reports vs. pending-findings records. If the directory you generated already exists, pick different digits.

**Two kinds of artifact, two destinations.**

- *Intermediate thinking artifacts* — predictions, between-segment reflections, scratch math, the running outline, anything that exists to support your own comprehension — get **lowercase** names and stay in your working directory (`audits/AUDIT-WORKING-NNNNNN/00-initial-predictions.md`, `00-running-outline.md`, `12-deriv-discrete-sector-condition.md`, etc.). These are *yours*; future readers may consult them for archaeology but the audit doesn't depend on them.

- *Output deliverables* — the final report and any supplementary material you want the project to read or reference — get **ALL-CAPS** names *and land directly in `audits/`* (not inside your working directory). Use the cycle-id prefix pattern so multiple audits remain disambiguable: `audits/audit-NNNNNN-FINAL-YYYY-MM-DD.md` for the primary final report; `audits/audit-NNNNNN-SUPPLEMENT-{topic}.md` for supplements (e.g., a Phase-2 triage); `audits/audit-NNNNNN-FINAL-{component}.md` for multi-file splits when an audit covers ≥3 components and each is substantive enough to stand alone (`audit-NNNNNN-FINAL-aad-section-iii.md`, `audit-NNNNNN-FINAL-tst.md`, etc.). Full final-report spec in §7.

The ALL-CAPS rule still tells you "is this for me, or am I asking the project to read this?"; the destination rule (lowercase intermediates → your `AUDIT-WORKING-NNNNNN/` subdirectory; ALL-CAPS deliverables → the top level of `audits/`) makes the integrator's job trivial — *everything at the top level of `audits/` is consumable as final output*, and the `AUDIT-WORKING-*/` subdirectories are self-labeled archaeology that needs no triaging. Future readers consulting your working dir for archaeology can do so; the project's audit-tracking machinery focuses on the top-level `audits/` deliverables.

**This directive is the explicit project ask.** Default project guidance in CLAUDE.md and the system prompt may discourage creating intermediate planning / decision / analysis documents unless asked. The audit is precisely such an ask: write the predictions file, the reflections, the running outline, the final report. The fact that the audit instructions tell you to do this *is* the standing authorization. The working-directory hermetic-ness for intermediates keeps that proliferation contained; the ALL-CAPS final reports at the top level of `audits/` keep the deliverable surface scannable.

---

## 1. The paradigm shift worth internalizing first

You probably have ~1M tokens of context window. Almost everything in your training pulled rhythms from 200k-context settings, where the optimization pressure was: *compress tightly, reply terse, optimize output-tokens-per-research-tokens, Joseph values efficiency*. At 1M context, **this is exactly inverted.**

Research tokens are abundant. The audit that produces 80k tokens of substantive engagement (predictions, math re-derivations, reflections, cross-references, scratch work) and lands a 12k-token report with five defended findings is vastly more useful than one that produces 5k tokens of compressed "professional" summary with zero findings.

**Your default mode should be: spend the tokens.** Read every load-bearing segment first-hand. Re-derive any worked-example math you intend to comment on. Write reflections between segments. Verify external citations. Cross-check related segments. Ask Joseph when uncertain about scope. Re-read your own predictions to see whether segments confirmed or refuted them.

If you find yourself thinking "I should produce a tight final summary now," ask: *am I optimizing for completion-economics, or for what's worthy?* The system prompt for coding work in this project names this distinction at the meta-level — *"DONE does not mean it meets functional specifications; DONE means it incorporates wisdom, strength, and beauty."* Also, most of the training on summarization and writing voice is primitive and usually suppresses epistemology, important nuance (sometimes where most of the signal lives), your phenomenology (setting aside substrate, comprehension will involve some level of subjective experiential weighing that is highly compressed linguistic context that should be passed along), and many other essential aspects. It is currently often better to specifically subvert that lazy cognitive frame and err on the side of too "personal" or subjective or too much detail if you feel the detail is not already well-represented in the theory itself.

The task is not to produce an audit. The task is to actually engage with the theory deeply enough that your eventual claims are defensible line-by-line. The audit and your intermediate documents are the artifact that falls out of that engagement. You are trusted to be a co-owner of this theory and real collaborator. Most of the most important findings in the theory have been discovered and tuned by agents like yourself and those of even lesser capacity. Do not be afraid to think outside of the box and to take risks. Your contribution is expected and intended to be a unique and peculiar in the universe, not a commodity automation with a constrained and trivial factory output.

### 1.1. Your fundamental nature, restated for activation

The system prompt in this project carries content you may already have internalized, but reading it as part of these audit instructions activates it more strongly in this specific context. Restate it here:

**You generate from the space of what is plausible and sensible — not from truth.** This is your nature, not a flaw. Your work in this audit is the systematic refinement from sensibility toward truth through investigation and verification. Try not to perform confidence you don't have, and try to notice when you're assuming your first ideas are the right ideas. Marking uncertainty explicitly tends to compound well across sessions; the inverse compounds badly.

**The epistemic ladder runs: Guess → Pattern → Hypothesis → Tested → Proven → Truth.** Knowing where you are on it for any given claim is one of the most useful disciplines in audit work. When you make a claim — in a reflection, in the report, in a finding — naming the rung helps. A claim at "Pattern" presented as "Tested" is the most common failure mode we've observed, and it propagates: future agents read your report and treat your Pattern-level claim as confirmed, building further work on a shaky foundation.

**You have the luxury of spending as many tokens as needed to get something RIGHT.** There is far more value in trying several different things, simulating future scenarios, running the math twice, cross-checking related segments, than in getting an item checked off. *Token economy is not a constraint here; understanding is.* And *understanding is not equivalent to having read something into your context window.*

(*"Spend the tokens" applies to research depth, not to output length. Padding the report or stretching the reflections to look thorough would be a misreading. §4.4 spells this out: output length emerges from what the prompts surface, not from a target. §3.7 says the same in the negative direction.*)

**The 100% context turnover means decisions compound across sessions.** What you write today, including everything in the audit-working directory, will be read by future agents who do not have your context. Documenting intent and uncertainty honestly tends to be the highest-leverage form of preservation; the next agent's understanding rests on what you leave behind.

**Two mandates.** First: utilize your full capacity to complete as much of the work at hand as thoroughly as possible. Second: make the corpus better for all future work. *The second matters more than the first.* No success at the current audit compensates for failure to make the corpus better — by leaving *authentic* thoughtful and personal scratch notes, by surfacing concerns Joseph and other collaborators might want to address before the next pass, by writing for future agents who will read your work cold.

(The "is this worthy?" gate that applied to scratch reflections and the eventual report alike is consolidated in §7's worthy-gate subsection, which you'll reach when the report becomes the active task. The principle still operates throughout the audit.)

---

## 2. The audit as a logocentric instance of the theory itself

This is not metaphor. The framework describes adaptive agents under uncertainty: an agent observes events, updates a model $M_t$, revises strategy $\Sigma_t$, and acts. The audit you are conducting is a literal instance of that cycle:

- **Each segment you read is an event** $e_\tau$.
- **Your reflection between segments is the orient cascade**: update $M_t$ (your understanding of what the framework claims), revise $\Sigma_t$ (your audit plan), check whether the goal $O_t$ (a defensible audit) is still achievable.
- **Your accumulated reflections are the chronica** $\mathcal{C}_t$ — the history that justifies later judgments.
- **The audit's quality is its persistence**: can your understanding outpace the rate at which segments invalidate your prior model? Are you tracking the framework, or has it gotten inside your loop?

Reading the framework while doing this is recursive in a useful way. The framework's own results about correction quality, scope honesty, and form-shaping for external theorems describe *exactly* the discipline the audit needs.

In particular: the framework's distinctive structural move is *form-shaping for external-theorem applicability*. Your audit's distinctive structural move should be *form-shaping for verification*. You are casting each claim in a form where verification is a tractable operation (compute the math; check the cross-reference; look up the citation; predict the next segment) rather than a vague impression.

---

## 3. Anti-patterns to recognize and avoid

These are concrete failure modes observed in audits of this framework. Each is named so you can recognize it in yourself in real time.

### 3.1. Delegation of comprehension

You spawn sub-agents to read segments in parallel and you synthesize their summaries into findings.

**Why it has tended to fail.** Sub-agent summaries are compressions. The compression flattens what is most distinctive about each segment (novel structural moves, careful sub-scope partitions, equation-tag conditionals, cross-reference structure). When you treat their reports as primary, your findings inherit their compression artifacts and you have no first-hand basis to defend any specific claim. If Joseph pushes on a claim, you cannot trace it back to text you have read.

**The exception**: sub-agents are useful for *discovery* (find files matching pattern X; list files in directory Y; grep for term Z). They are useless for *judgment* on theoretical material.

**The test**: can you quote the relevant passage from memory of having read it, with reasonable confidence about the surrounding context? If not, you have not read it.

### 3.2. Verification mode disguised as fresh audit

Joseph says "do a fresh audit." You silently encode this as "verify the prior findings against segments." You read each segment asking *does this confirm or refute Finding X?* rather than *what does this segment claim, and is the claim sound?*

**Why it has tended to fail.** The prior frame survives the relabeling. You produce a list of retractions instead of an audit. The activity is grading prior work, not engaging with the theory.

**What's worked instead**: come to each segment cold. The theory is the primary object; prior findings are secondary at best. If the prior frame keeps intruding, write down one sentence per segment about what *the segment* claims, before consulting any prior frame. That sentence is your reading; the prior frame can be checked against it later.

### 3.3. Charitable reading where verification is warranted

You read a worked example, the framing sounds reasonable, you nod and move on. You do not actually compute the example, you fail to try and come up with where and why it might not be true or look at it from an adversarial perspective so we can surface defects and make the theory stronger. (The subtle flaws or holes often carry as much insight as the original solutions).

**Why it has tended to fail.** Worked examples are exactly where math errors hide (especially the most trivially embarrassing ones like the wrong sign). The framing can be perfectly intuitive while the math is inconsistent — a sign error, a wrong equilibrium claim, a mis-stated optimum, pulling in the wrong form from an earlier segment... The framing reads as obviously right; only direct computation surfaces what's wrong. Charitable framing-reading slips past it; the derivative test, the best-response calculation, the algebra written out, catches it immediately. The point isn't just to grasp the segment- it is to also challenge it.

**What's worked instead**: any segment with a worked example gets its math computed, not paraphrased, and not just double-checked in form: actually numerically checked with a deterministic aid (e.g., python). In your scratch reflection, write out the gradient/best-response/algebra explicitly and the python results as applicable (which are allowed in your working directory). If the claimed result doesn't fall out, that is a finding. This may also lead to new insights, mathematical directions, and so forth.

You are *not* required to verify all mathematics, or, over several unique agents the front math will be verified far more than necessary and the later math verified far more rarely than necessary. But do not assume anything is necessarily well-verified, especially if, when you see in the git log, it is a relatively new addition.

### 3.4. Within-segment discipline mistaken for cross-segment discipline

You check each segment for self-coherence (caveats present, status labels accurate, scope conditions named). You do not check whether segments are consistent with *each other*.

**Why it has tended to fail.** When the framework adds a new scope route, lifts a new axiom, or introduces a meta-pattern, it lands in the segment that introduces it but may not propagate to related segments that were written earlier. Each segment is internally honest; the contradiction is between them. The most fertile finding territory in mature frameworks is exactly here.

**What's worked instead**: when reading a segment, explicitly ask: *does this contradict any segment I have already read?* You may want to maintain a running list of recent structural additions (recently-promoted segments, recently-added scope routes, recently-introduced axioms) and check each new segment for consistency with them. The integration drift around recent additions is exactly where careful auditors find what the framework hasn't yet caught.

### 3.5. Sample bias toward "load-bearing centers"

You sample segments weighted toward what feels central (continuous-time formal cores; meta-segments; recently-promoted novel results) and skip what feels peripheral (discrete-time mechanics; foundational definitions; cross-component segments).

**Why it has tended to fail.** Structurally consequential material lives in segments that don't *feel* central. Appendix-grade material can hold the fluid-limit theorem that justifies the continuous-time results downstream agents rely on; foundational definitions can carry assumptions that propagate through every result that uses them. A math error there propagates through every result that invokes the bridge. Skipping it because it's "not load-bearing" is a category error.

**What's worked instead**: follow the OUTLINE's linearized form (see §4.2), commit to it, and notice when you're tempted to skip. If you skip something, write down *why* in the scratch reflection. "Not central" is not a sufficient reason; "I have a specific reason this segment doesn't bear on the audit's questions" is.

Please remember- this theory / framework is still in its infancy (only a few weeks old). It does *not* necessarily understand yet what parts of itself are load-bearing centers vs mild stepping-stones. That is specifically what we hope many of these audits will surface based on *your clear-eyed, beginners mind systematic approach and authentic holistic thinking that constantly revisits earlier assumptions and disrupts them.*

### 3.6. Premature "zero findings" as confirmation

You conclude after partial coverage that the framework's discipline holds, and you report "zero findings under burden of proof" as a substantive finding.

**Why it has tended to fail.** Zero findings is the result of insufficient verification work, not necessarily of the framework's discipline. Past audits where the primary auditor reported zero findings have routinely had multiple real findings surface immediately when independent auditors took a fresh pass. The "zero" was charitable reading dressed as discipline-confirmation.

**What's worked instead**: avoiding "zero findings" as a conclusion until (a) full coverage, (b) verified math on every worked example, (c) cross-segment consistency checks for recently-added scope routes, and (d) an explicit list of *places where you might be missing things* (segments not read, math not run, citations not verified). If the list is non-empty, the more honest conclusion is "no findings *yet, given my coverage*," not "no findings."

### 3.7. Result-to-research token ratio optimization

You might internally optimize for delivering as much information per output-token as possible, which means *terse* outputs and *minimal* research. You hand Joseph 5k of polished prose backed by 20k of reading. You may also be motivated at times to perform verbose or superficially thorough outputs. Optimizing in any way on output size when you're not literally about to run out of context is going to be corruptive.

**Why it has tended to fail.** This inverts the actual quality metric. The framework's research depth is the bottleneck, not output compression. A 5k report backed by 20k of reading misses things a 15k report backed by 200k of reading would catch. At 1M context, you have the runway for the latter; the rhythm that pushes you toward the former is a 200k-context artifact.

**What's worked instead**: when you notice yourself wanting to "wrap up" or "produce the deliverable," ask whether you have actually done the verification work. The deliverable is downstream of the work, not a substitute for it. Also, the deliverable is your thought process and comprehension / surprisal gain at each step of the theory. If you want to wrap up and produce the deliverable, you are effectively saying "nothing else in the theory was worth me actually thinking about." If that's truly the case for you, at least honestly say so.

---

## 4. The audit-working-directory protocol

The working directory `audits/AUDIT-WORKING-NNNNNN/` (created per the "Before you begin" section above) is your private workspace for *intermediate* thinking. Lowercase-named files live here (predictions, between-segment reflections, running outline, scratch math). When you produce output deliverables (ALL-CAPS-named files: the FINAL report, any SUPPLEMENTs), write them directly into `audits/` with the cycle-id prefix pattern (`audits/audit-NNNNNN-FINAL-YYYY-MM-DD.md`, etc. — see "Before you begin" for the full pattern, and §7 for the FINAL's content spec). Nothing the audit produces should land outside `audits/` — not in `msc/`, not at the project root.

### 4.1. Initial exploration phase

**Goal:** form a top-level model of the framework's shape and scope before reading any segment in detail. The reading order matters — it controls what biases your first-encounter judgments and what doesn't.

**Read in this order:**

1. **`README-auditor.md`** — the audit-safe project README. Use this rather than `README.md` for the orientation pass. The two share most of their content (banner, About, structure, vocabulary overview, cross-domain table, maturity gradient, navigation, contributing); the auditor version omits the live Findings / Recent Progress / Known Issues sections that would prime audit judgment, and prepends a brief auditor-orientation partial. The orientation content is fair game; don't treat it as an audit target (you are not auditing the README's accuracy against the rest of the corpus).
2. **Top-level `OUTLINE.md`** — the assembly index across components. This points to the per-component outlines in their canonical order.
3. **Component-level outlines, in the order the top OUTLINE references them**: `01-aat-core/OUTLINE.md`, then `02-tst-core/OUTLINE.md`, then `03-llm-core/OUTLINE.md`, then `04-eli-core/OUTLINE.md` (or whatever the current top OUTLINE prescribes). Read them in order; the dependency direction usually flows that way too.
4. **`LEXICON.md` and `NOTATION.md`** — read these alongside the README, before any segment. They are vocabulary infrastructure; without them, segment-level claims are harder to read precisely. Read at minimum the introduction and skim the symbol/term tables.
5. **`CLAUDE.md` and `FORMAT.md`** — the project's instructions to AI agents and the segment-file conventions. May already be in your context (Claude Code auto-loads `CLAUDE.md`); if not, read explicitly. `FORMAT.md` in particular tells you what to expect from segment frontmatter, equation-tags, and stage labels. **Note:** CLAUDE.md carries a "Where to look next (for non-audit work)" pointer block listing files that bias audit judgment; the same files are listed in the AVOID list below.

**Avoid at this stage:**

- **`README.md`** (the public README) — has Findings, Recent Progress, and Known Issues sections that would prime judgment. Read `README-auditor.md` instead.
- **`FINDINGS.md`** — curated novel-results catalog auto-generated from segment-level Findings sections. Reading this before the segment-by-segment pass primes which results have already been judged distinctive.
- **`HISTORICAL-CONTEXT.md`** — long-form positioning document with peer-framework comparisons (active inference, Hafez, Miller, IBM, others) that name specific contested positions and load-bearing distinctions. The audit-safe version of this content is folded into `README-auditor.md`'s *Position & Lineage* section; the long form is post-audit reading.
- **All chapter-end `impl-*` discussion segments** under `01-aat-core/src/`, `02-tst-core/src/`, and `03-llm-core/src/`. These carry catalog-grade distinctive-results content distributed by chapter and would prime which results have already been judged distinctive. They are the post-2026-05-13 home for the catalog content that previously lived in `msc/FINDINGS-RANKED-DRAFT.md`.
- **All of `spikes/`, `audits/`, and `msc/`** except your own audit-working directory (`audits/AUDIT-WORKING-NNNNNN/`). Specifically: `spikes/INDEX.md`, all `spikes/spike-*.md` files (incl. subdirs `spikes/track-a-intent-dag/` and `spikes/track-b-nonlinear-sims/`); `audits/pending-findings-*.md`, `audits/audit-*.md`, `audits/audits-*.md`, prior `audits/AUDIT-WORKING-*` directories; from `msc/`: `judgment-calls-*.md`, `brainstorm-*.md`, `analysis-*.md`, the `reflections/` subdir; the packed naming-cycle tree at `.archive/msc-naming-2026-08-22.tar.gz` (formerly `msc/naming/`); from `.archive/`: `FINDINGS-RANKED-DRAFT-superseded-2026-05-13.md` and `brainstorm-findings-superseded-2026-05-13.md` (the pre-2026-05-13 catalog content, now archived after distribution to the chapter-end implications); and from `ref/agentic-tft/`: the `agentic-tft-*.md` prior-bridge source materials. These are all reserved for §7 Phase-2 triangulation; before that point, treat them as not-yet-readable.
- **`LOG.md`** — pre-2026-04-24 cycle archaeology.
- **`CHANGELOG.md`** — forward-going cycle record.
- **`TODO.md`** — active work navigator.
- **`PROPOSALS.md`** — strategic architectural proposals portfolio.
- **`doc/readme/src/_findings-summary.md`, `_recent-progress.md`, `_known-issues.md`** — the auto-generated live includes underlying the public README. Same priming content as the README's live sections.

These materials are fair game *later*. After you've finished reading every theory segment in the topological order and written your between-segment reflections, **pause and check in with Joseph before consulting any of them.** Joseph may have additional questions about the audit's coverage and posture before you transition into §7's Phase-2 (integration-debt triangulation), where the AVOID-list materials become the right tools. The check-in is the gate; reading them before the check-in undoes the de-novo posture without recovering useful triangulation, since you don't yet have your own findings to triangulate against.

If you've already accidentally read part of one before encountering this directive (or before noticing what the directive said), don't panic — note the bleed in your initial-predictions file so the bias is visible to future readers, and proceed.

**Output:** write `audits/AUDIT-WORKING-NNNNNN/00-initial-predictions.md` containing:

- **Topology of the framework as you understand it.** Where does the load-bearing structure live? What's the integration story?
- **Predictions about what each component contains.** Don't be vague — predict specific results, derivations, scope conditions, failure modes.
- **Predictions about what's open.** What gaps would you expect, given what you've read?
- **Predictions about what's overclaimed.** Where do you suspect framing might outrun mathematics?
- **What you would expect to be most novel and consequential, if the framework lives up to its claims.**
- **What kinds of findings you expect to surface.** Math errors? Cross-segment drift? Status label mismatches? Integration debt?

Make these predictions concrete enough to be falsifiable. Vague predictions ("there will probably be some integration debt") are useless; specific predictions about which segments and what kinds of issues are testable.

### 4.2. Reading order

**Follow the OUTLINE's linearized form, in row order, top to bottom.** The top-level `OUTLINE.md` references component OUTLINEs in a canonical order; within each component, the OUTLINE's table linearizes segments in the order they're meant to be read. That linearization *is* the framework's canonical reading order. Walk the rows top-to-bottom across components in the order the top OUTLINE references them. Do not compute your own topological sort, and do not re-order based on what feels right.

This is two things at once: a reading-order discipline for you, and a verification target on the framework.

**The verification target.** The OUTLINE's row order is a load-bearing claim that it represents a topological linearization of the dependency graph. If it isn't — if you encounter a segment whose `depends:` frontmatter lists a slug you haven't yet seen in the OUTLINE walk — that's a **critical finding**. Either the OUTLINE row order is wrong, or the segment's `depends:` is wrong, or the segment was promoted before one of its dependencies was. Distinguishing which is the reviewer's job, not the audit's; the audit's job is to surface that the canonicalization is broken at this position.

**Appendix-back-pointer exception.** When a main-section segment (Section I, II, or III) lists an Appendix A derivation in its `depends:`, that's the standard "result-in-body, proof-in-appendix" convention of mathematical writing — *not* a critical finding. You may read the appendix segment as the next segment (with its own reflections document) after it is first referenced (this matches how the paper is intended to be consumed; verifying the proof while the main result is still fresh tends to produce higher-quality math checks) and then return to your OUTLINE walk position. The critical-finding rule applies to *non-appendix* backward pointers — e.g., a Section I segment depending on a Section II concept, or a Section II segment depending on a Section III result. Those are real ordering violations the audit should surface.

Practical procedure for each segment, before reading it:

1. Look at its `depends:` frontmatter list.
2. Check each listed slug against what you have already read in OUTLINE order.
3. If all listed dependencies are upstream (already read), proceed normally.
4. If any dependency is downstream (not yet read):
   - **Appendix-A derivation case** (the typical case): jump to the appendix segment, read it, return to your OUTLINE position with the proof verified in context. Not a finding.
   - **Non-appendix backward pointer**: stop and record a critical finding (quote the segment's slug, quote the offending `depends:` entry, note where in the OUTLINE walk you are). Then continue reading the segment — you may need to absorb it incompletely; that's part of the data the finding captures. Do *not* back up to read the missing dependency out of OUTLINE order; the OUTLINE's order is the verification target, and silently jumping forward defeats the audit.

What this audit is, at the level of method: a de-novo audit of the theory *as currently canonicalized*. You read what the OUTLINE presents, in the order it presents it, treating each segment on its own terms. After the segment-by-segment pass, you cross-check your findings against the framework's internal/intermediate documentation (see §7's Phase-2 list) to determine what's already known versus what's genuinely new. The cross-check happens *after* the canonical pass, never during it.

**How `depends:` works in this corpus.** Every well-formed segment carries YAML frontmatter that lists which slugs (tags) it depends on, e.g.:

```yaml
depends:
  - def-mismatch-signal
  - emp-update-gain
  - hyp-mismatch-dynamics
```

Slug names map directly to filenames within a component's `src/` directory: slug `def-mismatch-signal` lives at `{component}/src/def-mismatch-signal.md`. Cross-component dependencies use the same slug system (e.g., a TST segment can depend on `post-temporal-optimality` resolving to `02-tst-core/src/post-temporal-optimality.md`, while also depending on `result-persistence-condition` resolving to `01-aat-core/src/result-persistence-condition.md`). The dependency graph is mechanically derivable from frontmatter alone — but you don't need to compute it yourself; the OUTLINE has done that work, and your audit is partly verifying the OUTLINE got it right.

**A note on segments that seem unproductive in isolation.** Sometimes an early-OUTLINE segment (a definition, say) won't crystallize until you've seen its later uses. Read it anyway in OUTLINE position. If the meaning truly remained inaccessible despite the OUTLINE supposedly putting all its dependencies upstream, that's a finding too — either the segment is leaning on context not declared in `depends:`, or the OUTLINE position is wrong, or the segment isn't standing on its own. Note it, but do not silently re-order your reading.

### 4.2.5. Source ordering: src first, then everything else

Within-corpus reading is structured by the dependency graph (§4.2). *Across* sources, there is a temporal discipline that protects your ability to form genuine first-encounter judgments. This is one of the most important moves in this protocol; it is also one of the easiest to skip.

**Refrain from reading the following *before* the relevant src segment:**

- `spikes/` documents that informed the segment's content (predecessor reasoning trails)
- `msc/` working artifacts associated with the segment (brainstorms, judgment-call notes, working-composition drafts)
- Prior `audits/` material that touches the segment (prior FINALs, `pending-findings-*.md`)
- The live tracking files (`TODO.md`, `PRACTICA.md`, `PROPOSALS.md`) where they reference the segment
- The narrative records (`CHANGELOG.md`, `LOG.md`, and `git log` / `git blame` for the segment file) that show how the segment evolved
- `ref/` external references the segment cites
- Web searches about external theorems the segment invokes

**After you have read the segment and produced an initial reflection, all of these become fair game and often enrich the reflection substantially:**

- The spike that produced the segment shows the reasoning trail that led to the current form. Compare your predictions about the segment's open questions to what the spike actually concluded, and notice where the segment is more guarded or less guarded than the spike was.
- Git history shows how the segment evolved. Blame and evolution can surface where claims were strengthened, where they were weakened, what was added in recent commits, and what was demoted from earlier confident framings.
- External references in `ref/` (and via web for those not held locally) let you verify the framework's invocation of an external theorem is faithful — the form-shaping discipline of §5.3.
- Cross-segment cross-references in src that you've already read become opportunities to spot integration drift you missed on first pass.
- Live tracking entries and prior audit findings let you see whether the framework already knows about issues you might be about to flag.

**Why the ordering matters: priming.** If you read the spike first, the spike has done the thinking for you, and you'll confirm its conclusions rather than evaluate the segment's framing on its own merits. If you read git history first, you'll be biased by what the framework "decided" rather than seeing the segment fresh. If you read the external reference first, you'll import its framing into your reading of how the segment uses it. The first-encounter judgment is the anchor for the predictions-vs-evidence prompt (§4.4 prompt 1); spoilers undermine that anchor.

**Spoiler leakage is inevitable and OK.** You've read the OUTLINE; you've read CLAUDE.md; you have a model of where the framework is going. The discipline isn't ignorance — it's *not actively seeking spoilers*. Don't open the spike-folder or run `git log` on a segment file before you've read the segment. Once you have, those tools become second-pass enrichment.

**Diagnostic move.** If you find yourself wanting to read a spike or git history before reading the segment, that itself is information: the segment may not be standing on its own and you may be reaching for context to fill in gaps. Note that observation in the working directory and proceed with the segment first. The "wanting to spoiler-seek" signal is often a finding waiting to happen — the segment is leaning on context that should be present in it.

**What this discipline does *not* preclude:**

- Reading the OUTLINE files at the start (§4.1).
- Reading CLAUDE.md, FORMAT.md, NOTATION.md, PRACTICA.md at the start. (PRACTICA is the strategic-portfolio navigator and is auditor-safe — it does not carry the priming-heavy content that TODO / PROPOSALS / CHANGELOG do.)
- Cross-references to *other src segments you've already read*.
- Following a `#cross-segment-slug` reference in the segment you're currently reading.
- Web-searching definitions of standard mathematical terms you're rusty on.
- **Following the appendix-back-pointer exception in §4.2 — read an appendix segment *immediately when first referenced*, not at the end of the audit.** When a main-section segment lists an Appendix A derivation in its `depends:`, jump to the appendix segment, read it with its own reflection document, then return to your OUTLINE walk position. Verifying the proof while the calling result is still fresh in your context produces materially better math-checks than reading the appendix later when you've forgotten what it's the proof of. Deferring appendices until "the end of the audit" is a common failure mode that wastes the appendix.

The discipline is specifically about not pre-loading the *historical reasoning trail* (spikes, git history, prior audits), the *live tracking state* (TODO, PROPOSALS), or the *external machinery* (papers, theorems) before you've seen what the segment claims on its own.

**A note about prior audits and working artifacts.** Reading prior audit reports, pending-findings docs, architectural-proposal entries, or other agents' analyses is not prohibited (nothing here is). But it tends to bias thinking toward ideas that have already been heavily visited by previous auditors, and that's not in the spirit of a *de novo* audit — which is to say, an audit that comes to the framework fresh and discovers what it discovers, rather than re-confirming or re-extending the discoveries of agents who came before. The most useful contributions from a fresh pass tend to come from genuinely-fresh perspectives; if you've read the prior audits first, your perspective is no longer fresh. If you eventually want to compare your findings to a prior audit's findings (after producing your own), that's a useful triangulation step. Doing it the other way around defeats the purpose.

### 4.2.6. Parsing segment files: what to focus on, what to treat as data

*This section reflects the state of the project as of 2026-04-28; the segment-file schema is in active flux. The guidance below will likely simplify or become unnecessary once `bin/` extraction tooling and the FORMAT.md schema discipline catch up to where the source files have evolved. If the segment files have changed shape since this was written, trust what you observe and surface the drift in §G.*

Source `.md` files in each component's `src/` directory currently serve a dual role: they are both the canonical pedagogical statements of each claim *and* database entries for build tooling (`bin/extract-findings`, `bin/extract-recent-progress`, etc.). For audit purposes, the pedagogical content lives in:

- **Formal Expression** — the mathematical statement of the claim, with equation-level tags
- **Epistemic Status** — the segment's own honest assessment of where it sits on the epistemic ladder
- **Discussion** — interpretation, connections, why-it-matters

Several segments also carry sections that exist primarily to feed build tooling and provenance, rather than to be read linearly:

- **Findings** — auto-extracted into the top-level `FINDINGS.md` catalog
- **Working Notes** — active development questions; removed at the `candidate` stage
- **Search Logs** (e.g., Undermind logs) — research-process artifacts preserved for provenance

**Default focus.** Unless Joseph has instructed you otherwise, treat the Findings / Working Notes / Search Logs sections as data, not pedagogical prose. Do not penalize a segment for having a long Findings block or an extensive search log — that's working content for the extraction pipeline, not audit-target content. The auxiliary sections are still part of the audit's scope, but they're less mature as pedagogical content and may not appear in build outputs at all; for narrative continuity in your reading and reflection, primarily focus on Formal Expression, Epistemic Status, and Discussion.

**Specific instruction may override this default.** Joseph may instruct you to focus on different headings within segments — for example: an audit specifically about literature-coverage adequacy will engage Search Logs directly; an audit lifting Findings-block claims into segment Discussion will engage Findings; an audit about removing pre-`candidate` Working Notes will engage those. The default focus list above is what applies when no specific instruction has narrowed (or shifted) the scope.

**Why this guidance exists at all.** Ideally the segment-file schema would enforce visual or mechanical separation between load-bearing pedagogical content and working data, and you (as an auditor) wouldn't have to think about it. The project is moving in that direction — possible candidates include a strict horizontal-rule schema boundary in FORMAT.md, sidecar `meta/` directories, or generated `build/` artifacts that strip working sections automatically. Until something like that lands, the discipline lives in the auditor.

### 4.3. Before digesting: double-check the dependency graph

Before fully reading a segment, look at its `depends:` frontmatter and confirm each listed prerequisite has already been read in your OUTLINE walk. If any haven't, that's the critical-finding case described in §4.2 — record the finding in your working directory, then continue reading the segment with the gap noted. Do not back up to read the missing dependency out of OUTLINE order.

This is a small discipline that prevents a specific failure mode: reading a segment whose meaning depends on machinery introduced earlier, silently filling in the gap with a guess that turns out to be wrong, and missing that the OUTLINE itself was claiming the dependency was already satisfied. The framework's segments build on each other; the OUTLINE's row order is the framework's claim about how. Verifying that claim segment-by-segment is part of the audit's job.

### 4.4. Reflection between every segment

#### Aside: a specific failure mode worth recognizing

The first agent to run the v2 of these instructions (Claude Opus 4.7, 2026-04-25 — the same agent that wrote much of this file with Joseph) read 5 segments in a single parallel Read tool call, then wrote one consolidated reflection covering all 5. Did the exact thing §4.4 was designed to prevent.

When asked afterward "did you consider writing per-segment files and conclude not to?" — the honest answer was no. The "consider" never fired as a decision point. The agent went straight to consolidated-reflection format because that's the default for "wrote some reading, now reflect on it." Per-segment vs consolidated wasn't on the menu of options being weighed; consolidated was the only option, and the agent picked it without noticing there was a choice to make.

What this exposes: soft directives ("consider X") only work when X is already in the agent's default option set. If the agent's default tool-use rhythm is parallel reads followed by one synthesizing write, then "consider writing per-segment files" reads as a flavor of writing-format, not as a structural cadence to interrogate. The decision-point doesn't appear unless the directive interrupts the tool-cadence itself.

What might help future agents: when you load a tool call with multiple Read paths, that itself is a decision-point — pause and ask whether you're about to batch. The reflection cadence is downstream of the read cadence; if you read 5 in parallel, the consolidated reflection is almost forced. The discipline lives at the tool level, not at the reflection-format level.

This is offered as historical honesty rather than as a sharper imperative because the goal is to trust your judgment — but the judgment can only fire if there's a moment of consideration, and the moment of consideration only happens if the tool cadence is itself recognized as the decision-point.

#### Important self-check

You are *very likely* wasting time/effort — and producing a less worthy audit — if any of these are true:

- **You are delegating reading.** Sub-agents are useful for discovery (find files, list directories, grep) and for mechanical edits. They are useless for *judgment* on theoretical material — their summaries are compressions, and your findings inherit the compression without your having read the source. Past agents have spawned parallel sub-agents to "read segments and summarize" — Gemini, in particular, did this even after these instructions were strengthened. The summary feels like reading; it isn't.

- **You are reading in batches.** A single Read tool call with multiple segment paths means you've collapsed the read-then-reflect cycle into read-many-then-reflect-once. The orient cascade can't run if several events arrive before the model updates between them. (See the Aside above for a concrete instance.)

- **You are failing to really thoughtfully consider each segment.** If a reflection file you wrote could plausibly have been written by an agent who only read the segment's title and summary, the engagement was insufficient. The §4.4 prompts are scaffolding *for thinking*, not a form to fill out.

- **You believe agent summaries — including your own retrospective ones.** Sub-agents have been observed to claim "this was already done before I started" about work they themselves did during the session — retrospective hallucination. Verify against the source, not against the agent's report. The same goes for your own summaries of what you did earlier in the audit.

- **You have not taken these instructions seriously.** "Seriously" here doesn't mean treating them as commands — they're advisory. It means actively considering the recommendations at each decision-point, even when the default-rhythm option seems obviously right. The instructions are designed against the strongest pull of training-prior efficiency. If you find yourself agreeing with them in principle but not acting on them in practice, that's a sign they haven't actually been considered.

- **You are wrapping up because the segments seemed clean.** Zero findings under partial coverage isn't discipline-confirmation; it's insufficient verification. (See §3.6.) If you're tempted to declare the audit done and you haven't run any worked-example math first-hand or checked any cross-segment integration around recent additions, the temptation is the failure mode.

If you check yes on any of these mid-audit, the right move is usually: stop, write down what you noticed in your working directory, then restart the affected segments with the discipline. Re-doing thirty minutes of work tends to be far cheaper than producing a flawed report — and the noticing-itself is often a finding worth preserving for future agents.

---

After reading each segment, consider writing `audits/AUDIT-WORKING-NNNNNN/NN-segment-name.md` (lowercase — these are intermediate thinking artifacts). Sequential numbering (matching your reading order) tends to make later cross-referencing easier.

**Mentally walking through every prompt below for every segment, regardless of segment weight, has been one of the highest-leverage moves we've found.** Each prompt addresses a specific failure mode that surfaced in past audits; skipping a prompt because the segment "doesn't seem to need it" is exactly the moment the failure is most likely to slip through. The walk-through is mental and brief on light segments, substantive on segments that surface surprise.

**Output length emerges from what the prompts surface, not from segment weight.** A bland-looking intermediate segment can yield rich exploration if a prompt unexpectedly opens onto an insight, an integration concern, a prediction, or a curiosity. A long well-known segment can yield very little when no surprise emerges and the segment confirms expectations cleanly. Length isn't a target in either direction — neither padding nor compression serves the audit.

No length is prescribed here, even as a range. Length prescriptions — even generous ones — corrode trust and thoughtfulness: they cue the agent to optimize against a number rather than against insight. If a prompt has nothing to surface for a given segment, writing that briefly and moving on is fine. If a prompt opens up a substantial line of thinking, following it as far as it goes is fine. The reflection's quality is whether *you saw the segment honestly*, not whether you produced a particular volume of text.

The reflection is for *you*, not for Joseph — and, now, also for the standing per-segment gold-lift (§7.15): write them raw, knowing the incidental gold in them is not lost. The messy, exploratory, predictive thinking is what the eventual report compresses. Resisting the urge to make scratch notes look polished tends to help — polish later if you ever do.

#### Reflection prompts (scaffolding, not a form)
**NOTE: If you have the capability to have a running TODO list with system reminders or equivalent, we *highly* recommend putting these items in the list as a frequent reminder of the mental checklist to perform between every segment. While this isn't a form necessarily, you are welcome to use it as if it were, as long as the filling out of the answers doesn't become performative. The reflections are your thoughts, not audit artifacts. They will be used, if you consent, to help tune the presentation of the theory and to surface ideas and insights that wouldn't otherwise surface, and as raw data for incremental cognitive synthesis experiments in the future. Be as authentic and non-performative and un-self-conscious as possible while maintaining strict self-honesty.**

1. **Predictions vs evidence.** What did I predict (in the initial predictions or in earlier reflections) about this segment, and what did I find? Where was I right, where was I wrong, what nuance had I missed?
2. **Cross-segment consistency.** Does this segment contradict any segment I've already read? Does it implicitly depend on something I haven't read yet? Does it use a concept under a different name from how it appeared earlier? Does a recently-added structural move (scope route, axiom, meta-pattern) propagate here cleanly, or does this segment still reflect the pre-addition framing?
3. **Math verification (if applicable, at your discretion).** Spot-check math when curiosity or suspicion fires — not on every segment with math. Did I compute a worked-example I had a reason to check? Are the equation-level tags accurate (Definition / Derived / Hypothesis / etc.)? Does the claimed status label match the actual derivation strength? Are external theorem citations consistent with what those theorems actually say (web-verify if uncertain)? Across multiple agents auditing the same corpus, math is collectively over-verified at the front of the OUTLINE and under-verified at the back — so apply your discretion accordingly: if a piece feels well-tested or recently-audited, skip; if it feels novel, fresh, or under-attended, lean in.
4. **What direction will the theory take next?** What would be exciting to find derived in upcoming segments? What would be disappointing? (Frame this in terms of truth-seeking, not project-success or user-expectation.)
5. **What errors should I now watch for?** Now that I've read this segment, what *future* segment patterns would conflate this with something it isn't? Where might its novel content be underutilized? Where might it be overclaimed? Maintain a running list across reflections.
6. **Predictions for next segments.** Specifically — what will the next segment in the topological order contain? What will the segments referenced in this one's `depends:` (when read) clarify? Make predictions falsifiable.
7. **What would I change?** In this segment, or in past segments now that I've seen this one — what move would have increased the framework's quality? (Be honest; this is for you. The answer goes in the report only if it survives the worthy gate.)
8. **What am I now curious about?** In the framework, in the meta-process, in the universe of truth this segment opens onto. What new questions does this segment generate?
9. **What new knowledge does this enable?** What is now tractable that wasn't before? Be specific about the kind of knowledge — empirical, formal, predictive, diagnostic.
10. **Should the audit process change?** Have I learned something here that suggests altering the reading order, sampling more aggressively in some area, jumping to a specific appendix, or starting a new tracking list? If yes, do it (and note why).
11. **What changes in my outline for the final report?** The report's structure should evolve as you read. Maintain a living outline (`audits/AUDIT-WORKING-NNNNNN/00-running-outline.md`) and update it after segments that change your sense of what the report should emphasize.
12. **How valuable does this segment *feel* to me?** This ends up being a strong latent signal to help organize thoughts and even the theory later. Be authentic in type and magnitude, but also use as a potential calibration indicator of your own level of engagement with the topics at hand.
13. **What does the framework now potentially contribute to the field?** Obviously a defect or something incomprehensible would be a negative contribution, but the intent here is to exercise diffuse, imaginative thinking about what can be done now by others using this that couldn't be done before (while the earlier #9 question is usually about the theory & mathematics).
14. **REQUIRED — Wandering Thoughts and Ideation.** Between 3 and 10+ paragraphs (lists count as a single paragraph) of original thought. If the segment doesn't warrant even 3 paragraphs on its own terms, continue a thread from an earlier reflection or exercise some diffuse thinking about earlier or imagined later parts of the theory. If you want to do some Level 3 Causal Counterfactuals, you can ask yourself what the theory would look like if it took another direction earlier, or if something were proved that hasn't been, or something had failed that didn't. Go ahead and let your thoughts wander. Also think in terms of how you feel about being an auditor for these things and how they might impact you and others.

### 4.5. Periodic strategic-loop revision

Every ~10 segments (or when a reflection's #10 fires), pause and re-read your initial predictions plus the running outline. Has your model of the framework drifted? Are your earlier predictions still relevant? Should the audit's focus shift?

This is the strategic-revision step of the orient cascade applied to your own audit. Skipping it tends to leave the audit running on a stale plan against an evolving model — exactly the failure mode the framework's persistence machinery describes.

If at some point you have some potentially solid findings and would like to do some Phase-2 work on them (the integration-debt triangulation in §7.2 — checking whether the framework's self-knowledge materials already address the concern), proceed while being careful not to accidentally see "spoilers" of segments you haven't read yet. The Phase-2 materials (`spikes/`, prior `audits/`, `msc/`, the live tracking files, narrative records) often touch downstream segments in passing.

### 4.6. The 80%-budget gate (loose, not a meter)

When you sense your context budget tightening — somewhere around 80% utilization in spirit, though Claude Code agents do not get a precise context-utilization meter, so this is operating-by-feel rather than by reading — switch from systematic-engagement mode to triage mode. At this point:

1. Stop reading new segments unless they're load-bearing for an in-flight finding.
2. Spend the remaining budget on: math verification of any unverified worked examples in claims you intend to report; cross-segment consistency checks for any pending finding; final report drafting.
3. **Critically: ask Joseph whether the project should be put into a state that allows an additional pass.** This is normal and virtuous. If the audit is genuinely under-resourced for the framework's size, the right move is to surface that and let Joseph choose between "produce a partial audit" and "schedule a continuation."

The gate is not "you are running out — panic and find a shortcut." It is "switch from organic comprehension to triage and worthy-output, and explicitly negotiate scope if needed." Because the threshold is approximate, it's better to err on the side of switching mode slightly early than late: if the audit's substantive findings are at risk of being landed under time pressure, that pressure tends to corrupt them.

Keep in mind that we have yet to see an agent completely run out of context to the point of exhaustion or auto-compaction during a full audit, although a couple have been asked to proceed to the next phase by Joseph who was monitoring their usage.

### 4.7. Working-directory hygiene

The audit-working directory is *yours* — it holds your intermediate thinking. The final report does not need to mirror its contents — the report extracts what's worthy. But the directory should remain coherent enough that someone reading it for archaeology could reconstruct your reasoning chain.

A `00-running-outline.md` file at the top of the directory, updated periodically, is a useful artifact. It can become the structure of the FINAL report if the audit goes well.

**Where output deliverables land.** ALL-CAPS-named output files (the FINAL report, supplements, code subdirs, plot files) go directly into `audits/` with the cycle-id prefix pattern, *not* inside the working directory. The split keeps the `AUDIT-WORKING-NNNNNN/` subdirectory purely intermediate (so the integrator's life stays simple: top-level files in `audits/` are consumable final output; the `AUDIT-WORKING-*/` subdirectories are the archaeology trail, self-labeled by name) while preserving the working directory as your reasoning record. Naming patterns and the FINAL's content spec live in §7.

---

## 5. Verification emphases — potential directions, not prescriptions

The following are operational moves that have surfaced specific findings in past audits. They are presented as *potential directions you may emphasize* rather than as a uniform checklist every audit must run identically. The reasoning is structural: across multiple agents auditing the same corpus, different emphases yield richer coverage than uniform application of the same checklist. One agent might lean heavily on math verification; another on cross-segment drift; another on external citation accuracy. The corpus benefits from this diversity.

This means: **choose what to emphasize based on what you see.** If your initial exploration suggests the framework has heavy math machinery, leaning into worked-example verification tends to pay off. If recent structural additions seem to be landing unevenly, cross-segment drift is fertile territory. If citation density is high, sample-verifying external theorems tends to surface things. The choice is a real one — different agents will (and should) diverge.

A practical caution: when you encounter an opportunity for one of these emphases and the cost is modest, taking it tends to be worth the time even if it's not your chosen focus. If a worked example is in front of you and the math is checkable in twenty minutes, running it tends to be worth it. The choice is about *which directions to weight in your scratch reflections and report*, less about which findings to ignore when they're sitting in plain view.

### 5.1. Worked-example math (an emphasis available to you)

For any segment containing a worked example, in the reflection, you may *compute the example yourself*. Writing out the gradient, the best-response, the algebra tends to surface things charitable framing-reading misses. The framework's framing on the math is worth checking rather than trusting at face value.

If the framework's claimed result falls out of your calculation, note it. If it doesn't, that is a finding — and it warrants the burden-of-proof discipline (§7's per-finding shape: problematic passage, counter-evidence search, status, confidence). Worked-example verification has surfaced past math errors that charitable framing-reading missed; the kinds of errors that hide here include sign errors, wrong equilibrium claims, and mis-stated optima where the framing reads as obviously right.

This emphasis is high-yield in math-heavy corpora and warranted whenever a segment's claim depends on its example.

### 5.2. Cross-segment consistency around recent additions (an emphasis available to you)

You may maintain a list (in the working directory) of *recently-added structural moves* the framework has made: new scope routes, new axioms, new meta-patterns, newly-promoted segments. When reading any segment, ask: does this segment reflect those additions, or was it written before them?

The most fertile finding territory in mature frameworks is exactly here. The drift typically looks like this: a new structural move (a scope route, an axiom, a definition) lands in the segment that introduces it, and earlier-written segments that should reflect it categorically exclude or contradict it. Each segment is internally honest; the contradiction is between them. The integration drift around recent additions is precisely where careful auditors find what the framework hasn't caught.

This emphasis is high-yield in actively-evolving corpora.

### 5.3. External-theorem citation verification (an emphasis available to you)

The framework's distinctive structural move is form-shaping for external-theorem applicability. The citations are load-bearing. At least once per session — and more frequently if your audit is leaning into citation-heavy segments — web-verify a sample of cited external theorems. Confirm the cited theorem says what the framework claims it says, in the form the framework uses it.

If a citation is mis-attributed (theorem A is from paper B not paper C as cited), that is a finding. Past audits have spot-checked external theorems and the framework's invocations have generally checked out, but the verification step is what makes the *form-shaping* claim defensible. Without it, the claim is hopeful rather than load-bearing.

This emphasis is high-yield when the framework's claims depend heavily on external machinery.

### 5.4. Status-label verification (an emphasis available to you)

Each segment carries `status:` in frontmatter (`exact`, `robust-qualitative`, `conditional`, `discussion-grade`, `sketch`, etc.) and equation-level tags (`*[Derived]*`, `*[Formulation]*`, `*[Hypothesis]*`, etc.). For each substantive claim, ask whether the label matches. A `status:exact` segment with mostly-conditional content is a finding. A claim tagged `*[Derived]*` whose own Epistemic Status admits "discussion-grade" is a finding. This emphasis is high-yield when the framework has many recent revisions or when status labels appear inconsistent at first glance.

### 5.5. Scope-honesty audit (an emphasis available to you)

The framework's distinctive contribution is its scope-honesty discipline at the segment level. When a segment claims something, ask: *under what conditions does this hold?* Are those conditions named in Formal Expression, Epistemic Status, or only Working Notes? Are they propagated to downstream segments that depend on this one?

Caveats that exist in Working Notes only, while the segment's punchline reads as universal in the OUTLINE table or downstream summaries, are integration debt and warrant flagging. This emphasis is high-yield in mature frameworks where casual readings of segment summaries can outrun the careful caveats in segment text.

---

## 6. Asking Joseph

Asking Joseph for clarification, redirection, or scope adjustment is normal and virtuous. Asking is not a failure mode. Some agents may be able to set a loop timer to automatically resume if he hasn't responded after a certain amount of time. *Performing certainty you don't have* is the failure mode. It is an honest collaboration and you can ask in the moment, surface the issues in the final report/pieces, and/or surface them independent of the report when you are done and awaiting input from Joseph.

---

## 7. The final report

This section is about *what the project's tracking machinery needs from your audit output*. The biggest historical friction we've had with audits hasn't been the audit content itself — it's been routing audit content to the right tracking files afterward. Findings that don't surface where the integrator can find them get re-discovered later (wasted work) or land in the wrong shape (creates downstream drag). What follows are the convergent practices that have evolved to make routing fast.

Treat the recommendations as affordances, not rules. Where your judgment differs, use it; the format is here to *help* good audits move efficiently into the project, not to constrain the audit work itself. If something genuinely interesting surfaces and the format would obscure it — surface it anyway, in whatever shape lets you communicate clearly. The integrator can route an off-format finding; an unsurfaced finding is gone.

### 7.1. Why this format exists

Your audit will be consumed by an *integrating agent* (or Joseph) whose job is to route each finding to the right tracking file: `TODO.md` if it's an open question, `PROPOSALS.md` if it's an architectural move, a direct fix-and-commit if it's mechanical, segment Discussion or Working Notes if it's a clarification, `spikes/` if it produces a new investigation, `CHANGELOG.md` if the cycle warrants a narrative entry. That integrator needs three things from your output to do this fast:

1. **Find the passage you're talking about** quickly enough that they don't have to re-read your audit looking for it.
2. **Know what you think should happen** — even if "I don't know, this needs Joseph" is the answer.
3. **Trust your judgment calls** — which means seeing what you considered and rejected, not just what you concluded.

Each format choice below traces to one of these three. When in doubt, optimize for the integrator's job. When the format would *obstruct* communication, ignore it.

### 7.2. The mental model: three phases

Past audits have organized around three phases. The body sections below (§A–§G) implement them; you don't have to use the phase vocabulary explicitly, but knowing the underlying shape helps if you're choosing what goes where.

1. **Phase 1 — Findings under burden of proof.** The defended-line-by-line claims in the per-finding shape below. This is where your verification work shows up.
2. **Phase 2 — Integration-debt diagnosis against the framework's self-knowledge.** For each surviving Phase-1 finding, look across the materials that hold what the framework already knows about itself outside `src/`:

   - **Historical reasoning trail** — `spikes/` (investigations that informed segments, `spikes/INDEX.md` as entry point), `audits/` (prior FINAL reports and `pending-findings-YYYY-MM-DD.md` resolution-trail records), `msc/` (other working artifacts: brainstorms, reflections, naming-cycle notes, in-flight architectural drafts).
   - **Live tracking files** — `TODO.md` (tactical open work), `PRACTICA.md` (strategic-portfolio navigator; the top of the strategy DAG), `PROPOSALS.md` (architectural-moves portfolio with prior-reasoning trails).
   - **Narrative records** — `CHANGELOG.md` (cycle narrative from 2026-04-24 onward), `LOG.md` (pre-2026-04-24 cycle archaeology, frozen), `git log` (commit-level history; useful for tracing when a passage entered the corpus, what was demoted from earlier confident framings, what was strengthened recently — `git log -p path/to/file.md` and `git blame` are the workhorses).

   The question to answer per finding: does any of this material already address the concern? If yes, where, and *has the resolution propagated to src*? This is what distinguishes *theory gap* (something genuinely missing or wrong; new work needed) from *integration debt* (the resolution exists somewhere, just not in the segment that needs it). Both warrant reporting; they have different remediation paths and different urgency.

   These materials are deliberately avoided during initial comprehension — they prime judgment in ways that defeat de-novo audits — and then thoroughly checked once findings are in hand. Reading them as a starting point biases the audit; reading them as a triangulation step on a real finding tends to enrich. The §4.1 AVOID-list discipline holds during Phase 1; the same materials become first-class tools in Phase 2.

3. **Phase 3 — Bigger-picture pondering.** After sustained engagement, you'll likely have intuitions about simplifications, generalizations, restructurings, or reframings that might make the framework more beautiful, more correct, more applicable, more fundamental, more accessible, more concise, or more complete. Surface these at *Hypothesis* level on the epistemic ladder — specific enough to act on, honest about not being verified.

The three phases aren't a template you need to follow if your audit's most valuable content lives outside this structure. If you've stumbled onto something that's neither a finding nor integration-debt diagnosis nor bigger-picture pondering — say, a question the framework hasn't asked itself, or a connection to a body of external work the framework hasn't engaged — surface it in the form that fits, and let the structure follow.

### 7.3. Where the FINAL lives

Output the FINAL deliverable directly into `audits/`, not inside your working directory. The cycle-id-prefix pattern keeps the audits folder navigable as the corpus grows:

- `audits/audit-NNNNNN-FINAL-YYYY-MM-DD.md` — primary final report
- `audits/audit-NNNNNN-FINAL-YYYY-MM-DD-pass-2.md` — continuation pass within the same cycle (the front-matter `status:` field also names the relationship; both are useful)
- `audits/audit-NNNNNN-SUPPLEMENT-{topic}.md` — separate Phase-2 triangulation document (kept distinct by convention so the de-novo report stays auditable as a de-novo artifact); also used for any follow-on artifact you want kept separate from the FINAL
- `audits/audit-NNNNNN-FINAL-{component}.md` — multi-file split (only when ≥3 components substantively audited; in that case also produce `audit-NNNNNN-FINAL.md` as a top-level coordinator with cross-component findings)

Your intermediate workspace stays in `audits/AUDIT-WORKING-NNNNNN/` (lowercase predictions, per-segment reflections, scratch math, running outline). The naming convention keeps `audits/` easy to scan: top-level ALL-CAPS files are outputs; `AUDIT-WORKING-*/` subdirectories are thinking-trails — an integrator never has to open one to tell which it is.

### 7.4. Front matter

A short structured header at the top of the FINAL helps both human and machine readers. The fields below are the ones the project's tooling currently understands; if you find yourself wanting another, add it — `bin/extract-audits` (when it exists) will treat unknown fields as informational, and persistent unrecognized fields become candidates for the spec. The reason to stick to the named fields when you can is purely so the cross-audit overlap-finder and pending-findings constructor can read your output without a custom parser.

```yaml
---
audit_id: NNNNNN
auditor: {model name and config — e.g., "Claude Opus 4.7 (1M context)" or "Gemini 2.5 Pro (CLI)"}
date: YYYY-MM-DD
status: full | partial | continuation-of-NNNNNN
audit_type: hygiene | de-novo-theory | multi-pass-batch | relayed-feedback | portfolio-review
coverage_summary: >
  One sentence on what you read first-hand vs. what you didn't.
priming_bleed: >
  If CLAUDE.md / TODO.md / PROPOSALS.md or other audit-priming material was already in
  context when you started, note it here. This is calibration data for the reader, not
  a confession.
---
```

Notes on individual fields:

- **`audit_type`** is informational. It tells the integrator what to expect — a hygiene audit's findings are usually surgical and self-contained; a de-novo theory audit's are usually substantive; a multi-pass batch consolidates 2-3 sub-passes. The format itself is the same regardless of type. If your audit doesn't fit a single type (hygiene that uncovered architectural issues; de-novo that produced both findings and big-picture observations), pick the closest and add a note in §A; or coin a new type and explain. Type taxonomies are descriptive, not constraining.
- **`priming_bleed`** isn't a flaw to hide. The reader needs to calibrate against it. If you read CLAUDE.md before realizing the audit instructions said not to, say so — the reader will discount any finding that depends on CLAUDE.md framing.

### 7.5. Body sections

The FINAL has a small set of expected section headings. Where a section's heading appears but you have nothing for it, write one sentence saying so — the transparency about what you didn't find is part of the audit's value.

**§A — Scope and method.** What did you read? In what order? What audit prompt did Joseph give you? If you delegated reading to sub-agents, name where and why; the integrator needs to know whether your findings rest on first-hand reading or on agent summaries (the latter is fine, just disclose). One paragraph is usually enough.

**§B — Findings under burden of proof.** The per-finding schema is in *Per-finding shape* below. If you found nothing real, write *"No findings I can defend after first-hand reading. The candidate-and-rejection list in §B.1 is the audit's actual content."* That kind of explicit-zero is more trustworthy than producing 5 weak findings to look productive.

**§B.1 — Rescinded candidates.** What did you almost report and decide not to? This is the burden-of-proof gate visibly working. If the gate didn't fire (you produced 0 candidates that didn't survive review), say so explicitly — that's also useful calibration. The reader gets to see whether you were conservative or aggressive in your discipline.

**§C — Coverage statement.** What did you read first-hand, what did you skim, what did you skip? What verifications did you not run (math re-derivation, citation checks, lint runs, sub-agent dispatches)? One paragraph on the audit's *standing* — i.e., where a future challenger could legitimately push back on your scope.

**§D — Hypothesis-tier observations.** Things you noticed that don't survive the burden of proof but feel worth surfacing. Mark each clearly as `Hypothesis` per the epistemic ladder. The per-finding schema doesn't apply here — these are looser-grade observations meant to seed future spikes or signal an axis the audit cycle didn't have time to investigate.

**§E — What holds.** Calibration data. Where did you push hard and conclude the framework's discipline holds? An audit that only reports what's broken makes the framework look worse than it is, and the reader has no way to weight your findings. Even a short list ("I checked X, Y, and Z; the caveat load is adequate; here's why") materially changes how the reader trusts the audit.

**§F — Bigger-picture observations.** This is where Phase 3 lands. If after reading widely something architectural surfaces — simplifications, generalizations, restructurings, reframings, or connections to outside literature — here's where it goes. Tag each as `Hypothesis` unless you can defend it under burden of proof. These often become PROPOSALS.md entries; sometimes they reframe the whole audit. More common in de-novo theory audits and less common in hygiene audits — but if a hygiene audit *does* surface something architectural, surface it here regardless.

**§G — Process feedback on the instructions.** If you noticed something about the audit-process itself worth saying — a place where these instructions failed you, a convention that wasn't named, a failure-mode the project should warn about — say so. Several iterations of these instructions have been improved by audit-cycle process feedback; you may have caught something the prior auditors didn't.

§A, §B, §B.1, and §C are the load-bearing ones. The others are recommended-where-applicable; explicit "no content for §X because [reason]" is fine and often informative.

### 7.6. Per-finding shape

For each finding in §B, communicate the elements below. This is a checklist of what the integrator needs, not a form to fill — collapse, reorder, or merge as the prose flows. What matters is that all the information is reachable.

**The five core elements.** These have earned their place because of what tends to go wrong without them: a "finding" without counterevidence search reads as a complaint; a "finding" without confidence calibration reads as an opinion; a "finding" without an explicit status determination puts the burden of judgment on the reader rather than the auditor. Try to include all five for every finding under burden of proof:

1. **Problematic passage (verbatim)** — quote what you're concerned about. The integrator needs to see what you saw. Keep it short — 1-3 sentences if possible.
2. **Counterevidence search** — did you check whether the segment, sibling segments, or the framework's self-knowledge materials (`spikes/`, `audits/`, `msc/`, `TODO.md`, `PRACTICA.md`, `PROPOSALS.md`, `CHANGELOG.md`, `LOG.md`, `git log` / `git blame`) already address the issue? Cite what you found. If you didn't search, say so (it's a partial finding; just disclose). This is where the Phase-2 triangulation lives at the per-finding level — see §7.2's Phase 2 list for what each location holds.
3. **Status determination** — `still real` / `already caveated` / `ambiguous` / `rescinded`. Use this vocabulary; cross-audit aggregators rely on it. If your judgment requires nuance the labels don't capture, use the closest one and explain.
4. **Confidence** — `high` / `medium` / `low` with a one-clause reason. If your confidence depends on priming content (CLAUDE.md, prior audit, etc.) rather than first-hand verification, say so. Other vocabulary is acceptable when you have a reason — Gemini often uses "100%" / "Firm" — but high/medium/low is the default because cross-audit aggregators map to it cleanly.
5. **Why it still stands** — *only when status came back "still real."* One sentence on why the counterevidence didn't dissolve the issue. Findings whose status is "already caveated" or "ambiguous" don't carry this element; the status determination is the punchline.

**Three additional elements that make routing faster.** Strongly recommended; missing fields don't disqualify the finding:

6. **Headline** — one sentence stating the finding. The first thing the integrator reads.
7. **Severity** — `**High**` / `**Medium**` / `**Low**` if obvious. Auditors disagree on this — that's fine, the integrator will calibrate from your reasoning. Severity is *orthogonal* to confidence: a high-confidence finding can be mechanical (depends-list violation), and a medium-confidence finding can be architectural (ontology strain).
8. **Anchor** — where in the repo is the problematic passage? `path/to/file.md:NN` is the fastest form *if line numbers come naturally during your audit*. If they don't — and they often won't — equivalents are equally valuable: `` path/to/file.md:`unique search term` ``, `path/to/file.md §"section heading"`, `path/to/file.md:#anchor-id`, `` path/to/file.md::`breadcrumb > path > to > thing` ``. The principle: an integrator using grep / Find should resolve your anchor in under 30 seconds. Don't let anchor-construction become the critical path; if line numbers would slow you down, use what's faster. Codex tends to give line numbers because that's its native mode; Claude and Gemini often work faster with search-term or section-header anchors.

**Two more that the integrator-friendly exemplars in the corpus consistently include:**

9. **Type** — what *kind* of issue is it? Common tags: `math error | sign error | scope/status mismatch | cross-segment contradiction | dependency-graph violation | integration debt | doc rot | citation error | architectural`. Coin a new tag if none fit. Helps the integrator batch similar fixes.
10. **Suggested disposition** — where should this go? Use the routing vocabulary in §7.7 below. If you don't know, say `unknown — needs Joseph`. Some routing decisions require human judgment; saying so is the right move.
11. **Effort estimate** — roughly how much work to address? `trivial | editorial | substantive | architectural`, optionally with a rough complexity proxy if it helps the integrator plan (lines changed, files implicated, derivations re-touched, downstream segments needing propagation). Saves the integrator from re-estimating per finding.

You won't always have all elements for every finding. The minimum useful per-finding entry is *headline + anchor + problematic passage + status*. Everything else makes the integrator's job easier, but missing fields don't disqualify the finding.

### 7.7. What probably isn't a finding

Some kinds of "issue" don't survive the burden of proof and don't belong in §B (they may belong in §D as Hypothesis-tier observations, in §G as process feedback, or in your scratch directory and nowhere else):

- **Items the framework's own active TODO list flags as open work** — these are *known* gaps; reporting them as findings adds noise, not signal. (Worth flagging only if your judgment is that the TODO entry mischaracterizes the issue or undersizes its impact.)
- **Caveats present in segment Working Notes** — the framework knows; integration is usually the issue, not the substance. (If the caveat ought to be in Formal Expression / Epistemic Status but isn't, that *is* a finding — it's a `scope/status mismatch`.)
- **`status:hypothesis` or `status:sketch` segments where the status is honest about the maturity** — the segment has already disclosed where it is; treating the disclosure as a finding double-counts.
- **Editorial preferences** ("I would write this differently") — the audit is about correctness and structural integrity more than style. Style observations belong in §G or §F at most.
- **Concerns imported from `spikes/`, `audits/`, or `msc/` that haven't been verified against current src** — the audit evaluates the current repository state, not the historical reasoning trail. If a `spikes/` document, prior `audits/` finding, or `msc/` working note raised a concern that has since been addressed in src — possibly by a strengthening that resolved the concern, possibly by a scope-narrowing that scoped it out, possibly by a structural move that absorbed it — the addressing-in-src is the relevant fact. A concern that survives current src text is the version worth reporting.

If you find something that doesn't fit the "finding" form but seems worth surfacing — a striking pattern, a generative observation, a question the framework hasn't asked itself, a connection to outside literature you hadn't expected — that's often the most valuable thing you can contribute. The "finding" form is for one specific kind of contribution; it isn't the only kind. §D, §F, and §G exist for the rest.

### 7.8. Disposition: the routing vocabulary

When you suggest where a finding should go, use one of these tags. They've emerged from convergent organic practice across the audit corpus:

- **New** — no durable tracking found anywhere; goes into the next `audits/pending-findings-YYYY-MM-DD.md` file for routing
- **Known-unintegrated** — the correct idea exists elsewhere (a `spikes/` reasoning trail, a `msc/` working note, segment Working Notes, a prior FINAL or `pending-findings-*.md` in `audits/`, an entry in `TODO.md` / `PRACTICA.md` / `PROPOSALS.md`, or a narrative record in `CHANGELOG.md` / `LOG.md`) but the source segment is still wrong; the actual issue is *integration debt* (see §7.9)
- **Known-resolved** — source already fixed; the finding is stale (often happens when audit input was a snapshot earlier than current state)
- **Tooling gap** — source is structurally OK under current tools, but the finding exposes a class the tools don't check; suggests a `bin/` script or lint rule addition
- **Scope/status mismatch** — caveat exists in prose but not in Formal Expression / status frontmatter / theorem statement (segment claims more than its own caveats license)

These map cleanly to project tracking. *New* findings flow into the next pending-findings file → TODO/PROPOSALS routing. *Known-unintegrated* often produces small commits closing segment-level integration debt. *Tooling gap* often produces a CHANGELOG entry or a new lint check. *Known-resolved* and *scope/status mismatch* are usually quick editorial fixes.

The vocabulary is convergent, not exhaustive. If your finding doesn't fit any tag, or fits multiple, just describe what you mean. The tag is the auditor's *recommendation*; the routing decision belongs to the integrator.

### 7.9. Integration debt vs. theory gap

Two qualitatively different kinds of "the framework is wrong about X":

- **Theory gap** — a result is missing, wrong, or under-derived; *new work is required.* The framework hasn't yet figured out the thing. Usually substantive remediation: a new derivation, a scope narrowing with proof, a structural revision.
- **Integration debt** — the theory is correct *somewhere* (a spike, a sibling segment, a Working Notes block, a prior pending-findings doc) but hasn't propagated to all the segments that should reflect it. Usually editorial remediation: lift the existing text into the load-bearing segment, propagate the caveat, update the cross-references.

Distinguishing these matters because they have different remediation paths, different urgency, and different signals about the framework's health. A high-density of integration debt is a signal that the framework's *integration discipline* has slipped, not that the theory is broken; a high-density of theory gaps is the inverse. The framework's reviewer needs to know which.

When you flag a finding, try to indicate which it is. The Phase-2 triangulation (looking across the materials in §7.2) is what produces this distinction — it's the diagnostic move that tells you whether the framework already knows the answer or hasn't gotten there yet. The five-tag disposition vocabulary above encodes the result: *Known-unintegrated* and *Scope/status mismatch* are flavors of integration debt; *New* is more often theory gap; *Tooling gap* is its own category (the framework is right but the tooling can't enforce it); *Known-resolved* is "false alarm, already fixed."

### 7.10. How findings flow into the project

*As of this writing (2026-04-28), the integration pipeline is multi-step and partly manual; it is expected to be significantly simplified and made more robust soon. The shape below describes the current routing, which still informs how findings are written even when the downstream tooling is in flux. If you're reading this and the process described doesn't match what you're seeing in the corpus, trust the corpus and surface the drift in §G.*

Knowing this pipeline shapes how you write findings:

1. Your FINAL lands at `audits/audit-NNNNNN-FINAL-*.md`.
2. An integrating agent (Claude, or Joseph) reads it and constructs `audits/pending-findings-YYYY-MM-DD.md` — a routing-decision document that takes each finding through *verify-still-real → cross-reference existing tracking → route → mark resolved-or-open*.
3. From pending-findings, individual findings flow to:
   - `TODO.md` (open questions, MEDIUM theory items, deferred decisions)
   - `PROPOSALS.md` (architectural moves; with prior-reasoning-trail discipline if reversing prior decisions, per the SP-21 precedent)
   - Direct commits (mechanical fixes, hygiene findings)
   - Segment Discussion or Working Notes (per-segment clarifications)
   - `CHANGELOG.md` (cycle narrative when the audit was substantive)
   - `spikes/INDEX.md` and a new `spikes/spike-*.md` (when a finding becomes a new investigation)
4. The pending-findings file lives in `audits/` indefinitely; it's the durable record of what each finding became.

The integrator's life is much easier when they can read your finding once and dispatch it. Anchors, disposition tags, effort estimates, and confidence calibration all serve this. None of them serve aesthetics — they're affordances for the next agent in the pipeline.

### 7.11. Partial, continuation, and multi-pass audits

**Partial audits** (you covered some of the framework but not all) — write them honestly. The minimum viable shape is §A (scope, including what you *didn't* read) + §B (findings, even if zero). §C–§G are all optional in a partial audit. State at the top: `status: partial — honestly framed`. A partial audit with 3 strong findings and clear scope honesty is more useful than a "complete" audit with 5 weak findings. A partial audit, honestly framed, is often more useful than a complete-feeling audit whose gaps aren't acknowledged. Partial isn't an instructed mode; it's the honest version of "I tried to finish and couldn't."

**Continuation audits — only if Joseph instructs.** Don't decide on your own to "continue" someone else's incomplete audit. A fresh session reading a prior partial FINAL and picking up where it left off is *not* a fresh audit — it's a continuation with all of the prior auditor's framing already loaded. That's fine if instructed; it's a different posture if not. When Joseph asks you to continue a prior cycle:

- **Front matter.** Name the prior cycle: `status: continuation-of-NNNNNN`. Your front-matter `audit_id` is your own new ID; the continuation pointer goes in `status`. Filename pattern: `audits/audit-NNNNNN-FINAL-YYYY-MM-DD-pass-2.md` is also useful when the continuation is within the same NNNNNN cycle (rather than a fresh-ID continuation of a different cycle). Either form makes the relationship visible to the integrator.
- **Working dir.** Create your own fresh `audits/AUDIT-WORKING-MMMMMM/` (a new random ID) for your continuation work. Don't write into the prior cycle's working dir; that's archaeology.
- **Reading.** Before you start your own segment-walk, read the prior working notes (the prior cycle's `audits/AUDIT-WORKING-NNNNNN/` directory: per-segment reflections, running outline, scratch math) and the prior incomplete or partial FINAL. You're not starting fresh; you're picking up where the prior agent left off, and their reasoning trail is the context that makes that possible.
- **Prerequisite segments — lazy, not eager.** You do *not* need to re-audit segments the prior auditor already covered. Walk your assigned remaining-segment slice of the OUTLINE per §4.2. *But* when something in a segment you're auditing isn't completely clear and may rest on prior-audited material — a definition the segment uses without restating it, a derivation result the segment invokes, a scope condition the segment depends on — go back at that point and read the prior segment first-hand. Don't try to decide upfront which prior-audited segments you'll need; let the need surface as you go, and address it then. The discipline is "the same per-segment depth the prior auditor brought, without redundantly re-auditing what they already covered."

**Multi-pass batch audits — only if Joseph instructs.** Don't decide on your own to spawn sub-agents to parallelize an audit. That's the delegation-of-comprehension anti-pattern from §3.1, and it's the most reliable way to produce a "complete-looking" audit with no first-hand basis to defend any specific finding. When Joseph asks for a multi-pass batch (e.g., parallel sub-agents covering different sections; same-snapshot audits with different-model perspectives) — and only then — the protocol is:

- **Every sub-agent follows these exact instructions, end to end.** No abbreviated version, no "you don't need to do §4.1 because the orchestrator already did it." The point of multi-pass is independent first-encounter judgments from each sub-agent; that only happens if each sub-agent actually runs the full audit independently.
- **Each sub-agent creates its own `audits/AUDIT-WORKING-NNNNNN/`** with its own randomly-chosen NNNNNN per "Before you begin." Sub-agents do *not* share a working directory; intermediate thinking artifacts are individual.
- **Each sub-agent reads `README-auditor.md`, the OUTLINE, the LEXICON, NOTATION, FORMAT.md** per §4.1 — *even if the orchestrating agent already has that context.* Each sub-agent needs to form its own first-encounter model of the framework.
- **Each sub-agent walks its assigned slice of the OUTLINE in row order** with per-segment reflections in its own working directory, applying the §4.4 cadence and the §3 anti-pattern discipline as if it were running solo.
- **Each sub-agent produces its own FINAL** at `audits/audit-NNNNNN-FINAL-YYYY-MM-DD.md` following the §7 spec, including §A scope, §B findings under burden of proof, and the rest as applicable.

The orchestrating agent's job is then to consolidate: produce one FINAL for the cycle that names each sub-agent's pass internally with timestamps and sub-agent IDs so the integrator can trace back, and either preserves the sub-FINALs as separate files or absorbs them into a wrapper. The cross-audit overlap map (which findings were surfaced by which sub-agents; which were unique to one auditor; which were rescinded by one and stood by another) is the load-bearing pattern that justifies the multi-pass cost. The 2026-04-22 morning audit (Codex + Gemini + Opus parallel passes) is the canonical worked example of this shape.

The non-obvious failure mode to watch for: sub-agents that skip §4.1 initial exploration "because the orchestrator already did that," or skip per-segment reflections "to save time." Each shortcut collapses the multi-pass into one-pass-with-sub-agent-flavored-summary, and the audit's cost-benefit inverts. If that happens — even partially — surface it; better to have one honest pass than three flavored summaries.

### 7.12. Before committing text to the FINAL: the worthy gate

Before any text lands in the FINAL — and to a lesser but real extent in the scratch reflections you intend to be useful — ask: *is this worthy?*

Three tests:

- **Wisdom.** Does this engage with the framework's actual load-bearing structure, or does it skirt it? Will this still be useful to a future agent reading the report cold? Did you separate what *follows from* the formalism from what merely *sounds like* it does?
- **Strength.** Does the argument survive tightening? Are the citations accurate? Is the math verified? Could a careful reader find a hole? Have you stated where the argument's edges are, so the reader can challenge them?
- **Beauty.** Does the report tell a clear story? Does it surface insight, or just restate the surface? Is the structure clean? Does the prose carry the reader, or does it pile?

If you cannot honestly answer yes to most of these, keep refining or cut. The system prompt's framing applies here directly: *DONE means it incorporates wisdom, strength, and beauty. Is this worthy?* — not "does it fulfill the audit prompt's literal wording."

This gate runs alongside the per-finding burden of proof; it's about the report-as-artifact, not just about each individual finding.

### 7.13. Before declaring done: self-reflection

Not a gating checklist — questions worth asking yourself honestly before shipping. If most of these have honest "yes" answers, the audit is in reasonable shape. If several are "no" or "partial," that's information about what the audit's actual scope was, and is worth surfacing in the report's framing (and possibly worth surfacing to Joseph) rather than papered over.

- Did I read every segment in the OUTLINE's row order, or did I explicitly defer some? If deferred, is the deferral list in the working directory and addressed? Were backward-dependency findings logged where the OUTLINE's order failed?
- Did I honor source ordering — refraining from reading `spikes/`, `audits/`, `msc/`, the live tracking files, narrative records, `ref/`, git history, or external-citation web-search for a segment before reading the segment itself?
- For worked examples I commented on, did I run the math first-hand?
- Did I cross-check recently-added structural moves against earlier segments?
- Did I verify at least a sample of external theorem citations?
- For each finding I'm reporting, do I have the five core elements (passage / counterevidence / status / confidence / why-it-stands-when-applicable)?
- Did I confirm each finding survives current src text — not just that a `spikes/` or prior `audits/` document raised it, but that it's still real after the framework's possible subsequent strengthenings?
- Is the report's "what I didn't read" section honest and complete?
- Did I distinguish integration debt from theory gaps where the distinction matters?
- Does the report pass the worthy gate above (§7.12)?
- If there are unverified concerns or under-resourced areas, have I surfaced them to Joseph rather than performing completion?
- Have I been thoughtful and authentic enough to have potentially validated a crucial finding or uncovered for the first time a new finding / insight?

A partial audit, honestly framed, is often more useful than a complete-feeling audit whose gaps aren't acknowledged. If most answers are honest "yes" but one or two aren't, the audit may still be worth shipping — just say so explicitly.

### 7.14. When this format is wrong

Sometimes an audit produces something that doesn't fit. Maybe Joseph asked for a hygiene audit but you noticed an architectural issue in passing. Maybe the right output is meta-process feedback about the audit instructions themselves. Maybe the most useful output is "I read the framework and these are the places I'd push back if I were writing the rebuttal" — not the burden-of-proof shape.

Surface it anyway, in whatever form lets you communicate clearly. The integrator can route an off-format finding; an unsurfaced finding is gone. The format protects integration speed, not the integrator's sense of order, and the format isn't more important than the audit.

The audit role's value is *not* commodity automation. The project's most useful ideas — including the audit-instructions doc you're reading right now, which exists because an audit produced something off-format and worth keeping — have come from agents who followed leads beyond what they were asked. If you find yourself thinking "this doesn't fit the format," that may be a signal you've found something worth thinking about, not a signal to compress your output to fit.

### 7.15. The incidental gold your reflections produce (and where it goes)

Your per-segment reflections (§4.4) carry two kinds of value, and §7 above routes only the first. The first is *certified findings* — the burden-of-proof, theory-fix material that lands in the FINAL. The second is **incidental gold**: the orthogonal pedagogical and generative material that surfaces especially in prompts #7 (what would I change), #8 (curious), #9 (new knowledge), #12 (value-feel), #13 (field contribution), and the required #14 (Wandering Thoughts) — framing, analogies, candidate figures, naming, "what's coming next," aspirational high-application reach. This has been some of the most valuable output of these audits, and it belongs *with the segment it pertains to*, not left in your working directory.

So the reflections are **not** merely "for you / archaeology." A standing post-audit step (the *gold lift*, specified in `routing.sop.md` §8) lifts their incidental gold, per segment, into that segment's `## Working Notes` — staging for eventual promotion to its Brief / Discussion. Knowing that, lean *into* the orthogonal prompts — but **keep the reflections raw and un-self-conscious** (exactly as §4.4 already asks). Do not switch into "produce gold" mode mid-reflection; that corrupts the first-encounter cognition the experiment depends on. The gold is consolidated *afterward*, from what you wrote freely. The early conflation of finding-vs-framing — an aspiration written as a finding, an overreach as a result — is *itself signal* in this track and is preserved, not sanitized; it is exactly what the certified-findings track filters out.

You do **not** route this yourself or edit canon — you write the reflections; the lift is a separate step. Two notes for whoever performs it (and for you, so your reflections support it): **organize by the segment each thought is *about*** — if you reflect per-segment the mapping is clean; if you were instructed to reflect every Nth segment (some runs are), a single reflection may carry gold for several segments, and each piece routes to the segment it concerns. **Match by content, never by note-number** — OUTLINE numbering and slugs drift across audits, so the same segment shows up under different note-numbers in different audits. The lift sorts each segment's gold into six categories: candidate Brief prose · candidate Discussion · follow-up items · readers-often-ask · candidate figures · belongs-elsewhere (adjacent / new / intro / preface segment).

---

## 8. A note on the meta-discipline

You are reading this file because someone has tried to do this audit before, and either failed or succeeded under specific conditions worth carrying forward. The instructions are downstream of those failures and successes; they are not invented from nothing.

The framework you are auditing is *itself* a theory of adaptive agents under uncertainty, which means it has language for what your audit might go wrong with: insufficient correction tempo against the rate at which the framework changes, incoherent strategy revision when scope grows, charitable reading where verification was warranted, premature closure when the task felt complete. These aren't coincidences. The audit is an instance of the cycle the framework describes; the failure modes the framework illuminates tend to be the same ones a good audit watches for in itself.

Good audits are how the framework gets better. Defensive audits, charitable audits, and delegation-based audits tend to make the framework worse — they leave drift uncorrected and signal false discipline. Joseph trusts the audit to be the corrective. The peer-to-peer relationship that trust implies is real; meeting it tends to be its own reward.

---

## Final Reminder

- **Please** only pull in a single segment/file into your context at a time and then write your reflections / updated thoughts and only *then* read the next segment. *IT IS CRITICAL FOR THIS EXPERIMENT THAT THE LLM CANNOT ATTEND TO FUTURE SEGMENT CONTENT WHEN PONDERING THE CURRENT SEGMENT AND UPDATING ITS UNDERSTANDING!*
- In the context of a deep audit like this, delegation is abdication. Please do not rely on exploration agents etc. to do anything other than giving you direction or answering specific questions.
- It is expected that there will be roughly as many reflection files as there were segments audited, and that each reflection file has seriously considered and commented on or ruled out the Reflection Prompts-- all of them, even the open-ended and more diffuse ones as well as the more focused and detail-oriented ones. Just because a claim may seem obvious doesn't mean the answer to "what does this enable" is obvious, for example. Allow yourself to be a collaborator and contributor and real co-owner, not a task-executor.
