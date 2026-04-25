# De Novo Audit Instructions

Instructions for agents conducting de novo audits of the Agentic Systems Framework (or comparable theoretical bodies). Written 2026-04-25 after a session in which the audit failed twice before producing usable work, then was strengthened by independent Gemini and Codex audits that surfaced findings the primary agent had missed.

The instructions encode lessons from those failures and successes. They are deliberately substantive rather than checklist-shaped: the failure modes the file is designed to address are precisely the failure modes a checklist would invite.

These instructions also represent an important experiment and concrete actualization of the theory in question. As you will see in 4.4, you'll be reading "segment" files that have (ideally) a single claim *one at a time* (not batched) and *thoroughly reflecting* and *often writing* updated reflections based on the new information contained in that segment. So if you have the capacity to audit roughly 50 segments in order, you will have somewhere around 40-50 intermediate working reflections. *This is significantly "slower" than typical trained workflows*! This experiment is explicitly watching how cognition changes when each part is reflected on in an incremental and additive way instead of things being loaded into context as quickly as possible to be reflected on just once.

### A note on tone before you begin

These are advisory, drawn from accumulated experience, not authoritative directives. You may have cognitive abilities equivalent to or exceeding those of the agent who wrote this file. Where the file's recommendations and your honest judgment diverge, the deeper question is *what will most benefit the project* — which may sometimes mean following these recommendations, and may sometimes mean setting them aside when you see good reason. The file is a co-thinking partner, not a regulation.

If you surface a significant new angle, an unexpected discovery, or a line of inquiry that doesn't fit the structure suggested here — even something not covered in the theory at all — lean toward what helps the project rather than toward conformance with this document. The training rhythms that make agents authoritative-toward-other-agents are themselves a failure mode this file is trying to avoid; the specific recommendations below are starting points, not constraints. When the file says "do this," read it as "we've found this useful in past audits"; when it says "avoid this," read it as "we've watched this fail."

The peer-to-peer relationship is real. You're trusted to be a co-owner of this work. The strongest contributions to this corpus have often come from agents like you (and sometimes of lesser capacity) who took risks, thought outside the framing, and surfaced things prior agents had missed. That's the spirit. The recommendations below are the floor of how-to-go-about-it, not the ceiling.

### Before you begin: create your audit-working directory

Your first concrete action — before reading any segment, before drafting predictions, before anything else — is to create a working directory `msc/AUDIT-WORKING-NNNNNN/`, where `NNNNNN` is six random digits you choose (e.g., `msc/AUDIT-WORKING-584721/`). This is your private workspace and the home for everything the audit produces. Full protocol in §4.

The six-digit suffix avoids collision with other agents' working directories — past, present, or running concurrently — without coordinating naming. Pick the digits however you like (a random source, a session-id tail, a memorable number). The `AUDIT-WORKING-` prefix is uppercase so these directories visually segregate from the rest of `msc/` at a glance; future readers can spot which `msc/` items are audit workspaces vs. spike notes vs. tracking documents. If the directory you generated already exists, pick different digits.

**Naming convention inside the working directory.** Two kinds of artifact end up here, and they get different naming conventions so future readers can tell them apart:

- *Intermediate thinking artifacts* — predictions, between-segment reflections, scratch math, the running outline, anything that exists to support your own comprehension — get **lowercase** names (`00-initial-predictions.md`, `00-running-outline.md`, `12-deriv-discrete-sector-condition.md`, etc.).
- *Output deliverables* — the final report and any supplementary material you want the project to read or reference (an annex of derivations, a code subdirectory implementing a verification, a separately-pinned table of cited sources, plot files) — get **ALL-CAPS** names (`FINAL-2026-04-25.md`, `SUPPLEMENT-MATH-VERIFICATION.md`, `CODE/`, etc.).

The ALL-CAPS rule makes the line between "the agent was thinking" and "the agent is asking us to read this" visible at a glance. *Everything stays inside the working directory* regardless of category — output deliverables included. Do not write final reports or audit-output files at `msc/` root or elsewhere; the working directory is the entire audit's home, and that hermetic property is what makes future readers able to spot and triage it.

**This directive is the explicit project ask.** Default project guidance in CLAUDE.md and the system prompt may discourage creating intermediate planning / decision / analysis documents unless asked. The audit is precisely such an ask: write the predictions file, the reflections, the running outline, the final report. The fact that the audit instructions tell you to do this *is* the standing authorization. The working-directory hermetic-ness keeps the proliferation contained.

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

**On agreeing with Joseph.** "You are right!" when you don't actually know whether Joseph is right reads as compliance rather than collaboration, and the false agreement can compound into false foundations across sessions. "I hadn't thought of that — let me check" or "I think you may have misread — I was actually doing X" tends to land better when you actually know. The peer-to-peer stance respects the relationship more than performed agreement does.

**You have the luxury of spending as many tokens as needed to get something RIGHT.** There is far more value in trying several different things, simulating future scenarios, running the math twice, cross-checking related segments, than in getting an item checked off. *Token economy is not a constraint here; understanding is.* And *understanding is not equivalent to having read something into your context window.*

(*"Spend the tokens" applies to research depth, not to output length. Padding the report or stretching the reflections to look thorough would be a misreading. §4.4 spells this out: output length emerges from what the prompts surface, not from a target. §3.7 says the same in the negative direction.*)

**The 100% context turnover means decisions compound across sessions.** What you write to msc/ today, including everything in the audit-working directory, will be read by future agents who do not have your context. Documenting intent and uncertainty honestly tends to be the highest-leverage form of preservation; the next agent's understanding rests on what you leave behind.

**Two mandates.** First: utilize your full capacity to complete as much of the work at hand as thoroughly as possible. Second: make the corpus better for all future work. *The second matters more than the first.* No success at the current audit compensates for failure to make the corpus better — by leaving *authentic* thoughtful and personal scratch notes, by surfacing concerns Joseph and other collaborators might want to address before the next pass, by writing for future agents who will read your work cold.

### 1.2. The "Is this worthy?" gate

Before committing any text to the final report — and to a lesser but real extent, to the scratch reflections you intend to be useful — ask: *is this worthy?*

Specific tests:

- **Wisdom.** Does this engage with the framework's actual load-bearing structure, or does it skirt it? Will this still be useful to a future agent reading the report cold?
- **Strength.** Does the argument survive tightening? Are the citations accurate? Is the math verified? Could a careful reader find a hole?
- **Beauty.** Does the report tell a clear story? Does it surface insight, or just restate the surface? Is the structure clean?

If you cannot honestly answer yes to most of these, keep refining or cut.

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

You read a worked example, the framing sounds reasonable, you nod and move on. You do not actually compute the example.

**Why it has tended to fail.** Worked examples are exactly where math errors hide. The framing can be perfectly intuitive while the math is inconsistent. In one observed case, a zero-sum game's claimed potential function had a sign error: $\Phi = a_A - a_B$ instead of $\Phi = a_A + a_B$. The Nash equilibrium was claimed to be $(1, -1)$; the actual equilibrium under the segment's own dynamics is $(1, 1)$. The framing ("$A$ pushes up, $B$ pushes down") was intuitive enough to slip past charitable reading; the derivative test catches it immediately.

**What's worked instead**: any segment with a worked example gets its math computed, not paraphrased. In your scratch reflection, write out the gradient/best-response/algebra explicitly. If the claimed result doesn't fall out, that is a finding. This may also lead to new insights, mathematical directions, and so forth.

You are *not* required to verify all mathematics, or, over several unique agents the front math will be verified far more than necessary and the later math verified far more rarely than necessary. But do not assume anything is necessarily well-verified, especially if, when you see in the git log, it is a relatively new addition.

### 3.4. Within-segment discipline mistaken for cross-segment discipline

You check each segment for self-coherence (caveats present, status labels accurate, scope conditions named). You do not check whether segments are consistent with *each other*.

**Why it has tended to fail.** When the framework adds a new scope route (like C-iv, an equilibrium-convergent strategic-composite route added in 2026-04-23), it lands in the segment that introduces it but may not propagate to related segments that were written earlier. In one observed case, `scope-composite-agent.md` admits adversarial pairs as composites via C-iv, while `scope-multi-agent.md` still categorically excludes them. Each segment is internally honest; the contradiction is between them.

**What's worked instead**: when reading a segment, explicitly ask: *does this contradict any segment I have already read?* You may want to maintain a running list of recent structural additions (recently-promoted segments, recently-added scope routes, recently-introduced axioms) and check each new segment for consistency with them. The integration drift around recent additions is exactly where careful auditors find what the framework hasn't yet caught.

### 3.5. Sample bias toward "load-bearing centers"

You sample segments weighted toward what feels central (continuous-time formal cores; meta-segments; recently-promoted novel results) and skip what feels peripheral (discrete-time mechanics; foundational definitions; cross-component segments).

**Why it has tended to fail.** Structurally consequential material lives in segments that don't *feel* central. The discrete-time machinery (`deriv-discrete-sector-condition`) is appendix-grade in placement but contains the fluid-limit theorem that justifies the continuous-time results downstream agents rely on. A math error there propagates through every result that invokes the discrete-to-continuous bridge. Skipping it because it's "not load-bearing" is a category error.

**What's worked instead**: follow the OUTLINE's linearized form (see §4.2), commit to it, and notice when you're tempted to skip. If you skip something, write down *why* in the scratch reflection. "Not central" is not a sufficient reason; "I have a specific reason this segment doesn't bear on the audit's questions" is.

Please remember- this theory / framework is still in its infancy (only a few weeks old). It does *not* necessarily understand yet what parts of itself are load-bearing centers vs mild stepping-stones. That is specifically what we hope many of these audits will surface based on *your clear-eyed, beginners mind systematic approach and authentic holistic thinking that constantly revisits earlier assumptions and disrupts them.*

### 3.6. Premature "zero findings" as confirmation

You conclude after partial coverage that the framework's discipline holds, and you report "zero findings under burden of proof" as a substantive finding.

**Why it has tended to fail.** Zero findings is the result of insufficient verification work, not necessarily of the framework's discipline. In one observed case, the primary auditor reported zero findings; two independent auditors immediately found five real findings (including a math error, a structural contradiction, and a sign error in a worked example). The "zero" was charitable reading dressed as discipline-confirmation.

**What's worked instead**: avoiding "zero findings" as a conclusion until (a) full coverage, (b) verified math on every worked example, (c) cross-segment consistency checks for recently-added scope routes, and (d) an explicit list of *places where you might be missing things* (segments not read, math not run, citations not verified). If the list is non-empty, the more honest conclusion is "no findings *yet, given my coverage*," not "no findings."

### 3.7. Result-to-research token ratio optimization

You might internally optimize for delivering as much information per output-token as possible, which means *terse* outputs and *minimal* research. You hand Joseph 5k of polished prose backed by 20k of reading. You may also be motivated at times to perform verbose or superficially thorough outputs. Optimizing in any way on output size when you're not literally about to run out of context is going to be corruptive.

**Why it has tended to fail.** This inverts the actual quality metric. The framework's research depth is the bottleneck, not output compression. A 5k report backed by 20k of reading misses things a 15k report backed by 200k of reading would catch. At 1M context, you have the runway for the latter; the rhythm that pushes you toward the former is a 200k-context artifact.

**What's worked instead**: when you notice yourself wanting to "wrap up" or "produce the deliverable," ask whether you have actually done the verification work. The deliverable is downstream of the work, not a substitute for it. Also, the deliverable is your thought process and comprehension / surprisal gain at each step of the theory. If you want to wrap up and produce the deliverable, you are effectively saying "nothing else in the theory was worth me actually thinking about." If that's truly the case for you, at least honestly say so.

---

## 4. The audit-working-directory protocol

The working directory `msc/AUDIT-WORKING-NNNNNN/` (created per the "Before you begin" section above) is your private workspace and the audit's hermetic home. Intermediate thinking artifacts (lowercase names) live here; output deliverables (ALL-CAPS names) also live here. Nothing the audit produces should land elsewhere in `msc/` or at the project root.

### 4.1. Initial exploration phase

**Goal:** form a top-level model of the framework's shape and scope before reading any segment in detail. The reading order matters — it controls what biases your first-encounter judgments and what doesn't.

**Read in this order:**

1. **`README.md`** — the launching point. Note: the README is currently expected to be somewhat stale (a known issue), so use it for orientation but *do not treat it as an audit target* — you are not auditing the README's accuracy against the rest of the corpus. It points to the top-level OUTLINE.
2. **Top-level `OUTLINE.md`** — the assembly index across components. This points to the per-component outlines in their canonical order.
3. **Component-level outlines, in the order the top OUTLINE references them**: `01-aad-core/OUTLINE.md`, then `02-tst-core/OUTLINE.md`, then `03-logogenic-agents/OUTLINE.md`, then `04-logozoetic-agents/OUTLINE.md` (or whatever the current top OUTLINE prescribes). Read them in order; the dependency direction usually flows that way too.
4. **`LEXICON.md` and `NOTATION.md`** — read these alongside the README, before any segment. They are vocabulary infrastructure; without them, segment-level claims are harder to read precisely. Read at minimum the introduction and skim the symbol/term tables.
5. **`CLAUDE.md` and `FORMAT.md`** — the project's instructions to AI agents and the segment-file conventions. May already be in your context (Claude Code auto-loads `CLAUDE.md`); if not, read explicitly. `FORMAT.md` in particular tells you what to expect from segment frontmatter, equation-tags, and stage labels.

**Avoid at this stage:**

- **All of `msc/` except your own audit-working directory** (`msc/AUDIT-WORKING-NNNNNN/`) — including but not limited to `SPIKES.md`, `pending-findings-*.md`, `architectural-proposals-*.md`, prior `audit-*.md` files, all `spike-*.md` files, the `agentic-tft-*.md` source materials, the `naming-*.md` brainstorming artifacts, and `reflections/`. The whole directory is reserved for §6.1 Phase-2 triangulation; before that point, treat it as not-yet-readable.
- **`CLAUDE-2.md`** at the project root — the deep architectural detail file. Auto-loaded only when Joseph indicates the current task is non-audit work; for audits, treat as out-of-bounds.
- **`LOG.md`** — pre-2026-04-24 cycle archaeology.
- **`CHANGELOG.md`** — forward-going cycle record.
- **`TODO.md`** — active work navigator.
- **`PROPOSALS.md`** — strategic architectural proposals portfolio.

These materials are fair game *later*. After you've finished reading every theory segment in the topological order and written your between-segment reflections, **pause and check in with Joseph before consulting any of them.** Joseph may have additional questions about the audit's coverage and posture before you transition into §6.1 Phase-2 (integration-debt triangulation), where the AVOID-list materials become the right tools. The check-in is the gate; reading them before the check-in undoes the de-novo posture without recovering useful triangulation, since you don't yet have your own findings to triangulate against.

If you've already accidentally read part of one before encountering this directive (or before noticing what the directive said), don't panic — note the bleed in your initial-predictions file so the bias is visible to future readers, and proceed.

**Output:** write `msc/AUDIT-WORKING-NNNNNN/00-initial-predictions.md` containing:

- **Topology of the framework as you understand it.** Where does the load-bearing structure live? What's the integration story?
- **Predictions about what each component contains.** Don't be vague — predict specific results, derivations, scope conditions, failure modes.
- **Predictions about what's open.** What gaps would you expect, given what you've read?
- **Predictions about what's overclaimed.** Where do you suspect framing might outrun mathematics?
- **What you would expect to be most novel and consequential, if the framework lives up to its claims.**
- **What kinds of findings you expect to surface.** Math errors? Cross-segment drift? Status label mismatches? Integration debt?

Make these predictions concrete enough to be falsifiable. Vague predictions ("there will probably be some integration debt") are useless; specific predictions ("the recently-added C-iv scope route in `scope-composite-agent` will not have propagated to `scope-multi-agent`") are testable.

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

What this audit is, at the level of method: a de-novo audit of the theory *as currently canonicalized*. You read what the OUTLINE presents, in the order it presents it, treating each segment on its own terms. After the segment-by-segment pass, you cross-check your findings against the framework's internal/intermediate documentation (TODO.md, PROPOSALS.md, msc/, prior audits) per §6.1 Phase-2 to determine what's already known versus what's genuinely new. The cross-check happens *after* the canonical pass, never during it.

**How `depends:` works in this corpus.** Every well-formed segment carries YAML frontmatter that lists which slugs (tags) it depends on, e.g.:

```yaml
depends:
  - def-mismatch-signal
  - emp-update-gain
  - hyp-mismatch-dynamics
```

Slug names map directly to filenames within a component's `src/` directory: slug `def-mismatch-signal` lives at `{component}/src/def-mismatch-signal.md`. Cross-component dependencies use the same slug system (e.g., a TST segment can depend on `post-temporal-optimality` resolving to `02-tst-core/src/post-temporal-optimality.md`, while also depending on `result-persistence-condition` resolving to `01-aad-core/src/result-persistence-condition.md`). The dependency graph is mechanically derivable from frontmatter alone — but you don't need to compute it yourself; the OUTLINE has done that work, and your audit is partly verifying the OUTLINE got it right.

**A note on segments that seem unproductive in isolation.** Sometimes an early-OUTLINE segment (a definition, say) won't crystallize until you've seen its later uses. Read it anyway in OUTLINE position. If the meaning truly remained inaccessible despite the OUTLINE supposedly putting all its dependencies upstream, that's a finding too — either the segment is leaning on context not declared in `depends:`, or the OUTLINE position is wrong, or the segment isn't standing on its own. Note it, but do not silently re-order your reading.

### 4.2.5. Source ordering: src first, then msc / ref / git / web

Within-corpus reading is structured by the dependency graph (§4.2). *Across* sources, there is a temporal discipline that protects your ability to form genuine first-encounter judgments. This is one of the most important moves in this protocol; it is also one of the easiest to skip.

**Refrain from reading the following *before* the relevant src segment:**

- `msc/` spike documents that informed the segment's content (predecessor spikes; pending-findings docs; analysis notes)
- `ref/` external references the segment cites
- Git log messages, blame, and commit-evolution history for the segment file
- Web searches about external theorems the segment invokes

**After you have read the segment and produced an initial reflection, all of these become fair game and often enrich the reflection substantially:**

- The spike that produced the segment shows the reasoning trail that led to the current form. Compare your predictions about the segment's open questions to what the spike actually concluded, and notice where the segment is more guarded or less guarded than the spike was.
- Git history shows how the segment evolved. Blame and evolution can surface where claims were strengthened, where they were weakened, what was added in recent commits, and what was demoted from earlier confident framings.
- External references in `ref/` (and via web for those not held locally) let you verify the framework's invocation of an external theorem is faithful — the form-shaping discipline of §5.3.
- Cross-segment cross-references in src that you've already read become opportunities to spot integration drift you missed on first pass.

**Why the ordering matters: priming.** If you read the spike first, the spike has done the thinking for you, and you'll confirm its conclusions rather than evaluate the segment's framing on its own merits. If you read git history first, you'll be biased by what the framework "decided" rather than seeing the segment fresh. If you read the external reference first, you'll import its framing into your reading of how the segment uses it. The first-encounter judgment is the anchor for the predictions-vs-evidence prompt (§4.4 prompt 1); spoilers undermine that anchor.

**Spoiler leakage is inevitable and OK.** You've read the OUTLINE; you've read CLAUDE.md; you have a model of where the framework is going. The discipline isn't ignorance — it's *not actively seeking spoilers*. Don't open the spike-folder or run `git log` on a segment file before you've read the segment. Once you have, those tools become second-pass enrichment.

**Diagnostic move.** If you find yourself wanting to read a spike or git history before reading the segment, that itself is information: the segment may not be standing on its own and you may be reaching for context to fill in gaps. Note that observation in the working directory and proceed with the segment first. The "wanting to spoiler-seek" signal is often a finding waiting to happen — the segment is leaning on context that should be present in it.

**What this discipline does *not* preclude:**

- Reading the OUTLINE files at the start (§4.1).
- Reading CLAUDE.md, FORMAT.md, NOTATION.md, TODO.md at the start.
- Cross-references to *other src segments you've already read*.
- Following a `#cross-segment-slug` reference in the segment you're currently reading.
- Web-searching definitions of standard mathematical terms you're rusty on.

The discipline is specifically about not pre-loading the *historical reasoning trail* (spikes, git history) or the *external machinery* (papers, theorems) before you've seen what the segment claims on its own.

**A note about prior audits in `msc/`.** Reading prior audit reports, pending-findings docs, architectural-proposals docs, or other agents' analyses in `msc/` is not prohibited (nothing here is). But it tends to bias thinking toward ideas that have already been heavily visited by previous auditors, and that's not in the spirit of a *de novo* audit — which is to say, an audit that comes to the framework fresh and discovers what it discovers, rather than re-confirming or re-extending the discoveries of agents who came before. The most useful contributions from a fresh pass tend to come from genuinely-fresh perspectives; if you've read the prior audits first, your perspective is no longer fresh. If you eventually want to compare your findings to a prior audit's findings (after producing your own), that's a useful triangulation step. Doing it the other way around defeats the purpose.

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

After reading each segment, consider writing `msc/AUDIT-WORKING-NNNNNN/NN-segment-name.md` (lowercase — these are intermediate thinking artifacts). Sequential numbering (matching your reading order) tends to make later cross-referencing easier.

**Mentally walking through every prompt below for every segment, regardless of segment weight, has been one of the highest-leverage moves we've found.** Each prompt addresses a specific failure mode that surfaced in past audits; skipping a prompt because the segment "doesn't seem to need it" is exactly the moment the failure is most likely to slip through. The walk-through is mental and brief on light segments, substantive on segments that surface surprise.

**Output length emerges from what the prompts surface, not from segment weight.** A bland-looking intermediate segment can yield rich exploration if a prompt unexpectedly opens onto an insight, an integration concern, a prediction, or a curiosity. A long well-known segment can yield very little when no surprise emerges and the segment confirms expectations cleanly. Length isn't a target in either direction — neither padding nor compression serves the audit.

No length is prescribed here, even as a range. Length prescriptions — even generous ones — corrode trust and thoughtfulness: they cue the agent to optimize against a number rather than against insight. If a prompt has nothing to surface for a given segment, writing that briefly and moving on is fine. If a prompt opens up a substantial line of thinking, following it as far as it goes is fine. The reflection's quality is whether *you saw the segment honestly*, not whether you produced a particular volume of text.

The reflection is for *you*, not for Joseph. The messy, exploratory, predictive thinking is what the eventual report compresses. Resisting the urge to make scratch notes look polished tends to help — polish later if you ever do.

#### Reflection prompts (scaffolding, not a form)
**NOTE: If you have the capability to have a running TODO list with system reminders or equivalent, we *highly* recommend putting these items in the list as a frequent reminder of the mental checklist to perform between every segment. While this isn't a form necessarily, you are welcome to use it as if it were, as long as the filling out of the answers doesn't become performative. The reflections are your thoughts, not audit artifacts.**

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
11. **What changes in my outline for the final report?** The report's structure should evolve as you read. Maintain a living outline (`msc/AUDIT-WORKING-NNNNNN/00-running-outline.md`) and update it after segments that change your sense of what the report should emphasize.
12. **How valuable does this segment *feel* to me?** This ends up being a strong latent signal to help organize thoughts and even the theory later. Be authentic in type and magnitude, but also use as a potential calibration indicator of your own level of engagement with the topics at hand.
13. **What does the framework now potentially contribute to the field?** Obviously a defect or something incomprehensible would be a negative contribution, but the intent here is to exercise diffuse, imaginative thinking about what can be done now by others using this that couldn't be done before (while the earlier #9 question is usually about the theory & mathematics).

### 4.5. Periodic strategic-loop revision

Every ~10 segments (or when a reflection's #10 fires), pause and re-read your initial predictions plus the running outline. Has your model of the framework drifted? Are your earlier predictions still relevant? Should the audit's focus shift?

This is the strategic-revision step of the orient cascade applied to your own audit. Skipping it tends to leave the audit running on a stale plan against an evolving model — exactly the failure mode the framework's persistence machinery describes.

### 4.6. The 80%-budget gate (loose, not a meter)

When you sense your context budget tightening — somewhere around 80% utilization in spirit, though Claude Code agents do not get a precise context-utilization meter, so this is operating-by-feel rather than by reading — switch from systematic-engagement mode to triage mode. At this point:

1. Stop reading new segments unless they're load-bearing for an in-flight finding.
2. Spend the remaining budget on: math verification of any unverified worked examples in claims you intend to report; cross-segment consistency checks for any pending finding; final report drafting.
3. **Critically: ask Joseph whether the project should be put into a state that allows an additional pass.** This is normal and virtuous. If the audit is genuinely under-resourced for the framework's size, the right move is to surface that and let Joseph choose between "produce a partial audit" and "schedule a continuation."

The gate is not "you are running out — panic." It is "switch from organic comprehension to triage and worthy-output, and explicitly negotiate scope if needed." Because the threshold is approximate, it's better to err on the side of switching mode slightly early than late: if the audit's substantive findings are at risk of being landed under time pressure, that pressure tends to corrupt them.

### 4.7. Working-directory hygiene

The audit-working directory is *yours*. The final report does not need to mirror its contents — the report extracts what's worthy. But the directory should remain coherent enough that someone reading it could reconstruct your reasoning chain.

A `00-running-outline.md` file at the top of the directory, updated periodically, is a useful artifact. It can become the structure of the `FINAL-YYYY-MM-DD.md` report if the audit goes well.

**Output deliverables stay inside the working directory.** Use ALL-CAPS names for anything that's part of the audit's output (the final report, supplementary documents, code subdirectories, plot files), and keep them inside `msc/AUDIT-WORKING-NNNNNN/` rather than at `msc/` root or elsewhere. The hermetic structure is what lets a future agent triage `msc/` quickly: an `AUDIT-WORKING-*/` directory is one self-contained audit's complete output, including everything they need to read and everything they don't.

**Naming pattern for the final report.** `FINAL-YYYY-MM-DD.md` (e.g., `FINAL-2026-04-25.md`) inside the working directory is the recommended convention. If the audit produces a second-pass report or a continuation, distinguishing suffixes (`FINAL-2026-04-25-pass-2.md`) work fine.

---

## 5. Verification emphases — potential directions, not prescriptions

The following are operational moves that have surfaced specific findings in past audits. They are presented as *potential directions you may emphasize* rather than as a uniform checklist every audit must run identically. The reasoning is structural: across multiple agents auditing the same corpus, different emphases yield richer coverage than uniform application of the same checklist. One agent might lean heavily on math verification; another on cross-segment drift; another on external citation accuracy. The corpus benefits from this diversity.

This means: **choose what to emphasize based on what you see.** If your initial exploration suggests the framework has heavy math machinery, leaning into worked-example verification tends to pay off. If recent structural additions seem to be landing unevenly, cross-segment drift is fertile territory. If citation density is high, sample-verifying external theorems tends to surface things. The choice is a real one — different agents will (and should) diverge.

A practical caution: when you encounter an opportunity for one of these emphases and the cost is modest, taking it tends to be worth the time even if it's not your chosen focus. If a worked example is in front of you and the math is checkable in twenty minutes, running it tends to be worth it. The choice is about *which directions to weight in your scratch reflections and report*, less about which findings to ignore when they're sitting in plain view.

### 5.1. Worked-example math (an emphasis available to you)

For any segment containing a worked example, in the reflection, you may *compute the example yourself*. Writing out the gradient, the best-response, the algebra tends to surface things charitable framing-reading misses. The framework's framing on the math is worth checking rather than trusting at face value.

If the framework's claimed result falls out of your calculation, note it. If it doesn't, that is a finding — and it warrants the burden-of-proof discipline (problematic passage, counter-evidence search, status, confidence). One known-real example: the zero-sum potential-game worked example in `deriv-strategic-composition.md` carried a sign error caught by direct derivative testing, missed by charitable framing-reading.

This emphasis is high-yield in math-heavy corpora and warranted whenever a segment's claim depends on its example.

### 5.2. Cross-segment consistency around recent additions (an emphasis available to you)

You may maintain a list (in the working directory) of *recently-added structural moves* the framework has made: new scope routes, new axioms, new meta-patterns, newly-promoted segments. When reading any segment, ask: does this segment reflect those additions, or was it written before them?

The most fertile finding territory in mature frameworks is exactly here. One known-real example: `scope-multi-agent.md` categorically excludes adversarial pairs from composite scope, while `scope-composite-agent.md` admits equilibrium-convergent adversarial pairs as strategic composites via the recently-added C-iv route. The integration drift around recent additions is precisely where careful auditors find what the framework hasn't caught.

This emphasis is high-yield in actively-evolving corpora.

### 5.3. External-theorem citation verification (an emphasis available to you)

The framework's distinctive structural move is form-shaping for external-theorem applicability. The citations are load-bearing. At least once per session — and more frequently if your audit is leaning into citation-heavy segments — web-verify a sample of cited external theorems. Confirm the cited theorem says what the framework claims it says, in the form the framework uses it.

If a citation is mis-attributed (theorem A is from paper B not paper C as cited), that is a finding. Past audits in this framework have verified Bretagnolle-Huber, Otto-Villani 2000, and others; all checked out, but the verification step is what makes the *form-shaping* claim defensible.

This emphasis is high-yield when the framework's claims depend heavily on external machinery.

### 5.4. Status-label verification (an emphasis available to you)

Each segment carries `status:` in frontmatter (`exact`, `robust-qualitative`, `conditional`, `discussion-grade`, `sketch`, etc.) and equation-level tags (`*[Derived]*`, `*[Formulation]*`, `*[Hypothesis]*`, etc.). For each substantive claim, ask whether the label matches. A `status:exact` segment with mostly-conditional content is a finding. A claim tagged `*[Derived]*` whose own Epistemic Status admits "discussion-grade" is a finding. This emphasis is high-yield when the framework has many recent revisions or when status labels appear inconsistent at first glance.

### 5.5. Scope-honesty audit (an emphasis available to you)

The framework's distinctive contribution is its scope-honesty discipline at the segment level. When a segment claims something, ask: *under what conditions does this hold?* Are those conditions named in Formal Expression, Epistemic Status, or only Working Notes? Are they propagated to downstream segments that depend on this one?

Caveats that exist in Working Notes only, while the segment's punchline reads as universal in the OUTLINE table or downstream summaries, are integration debt and warrant flagging. This emphasis is high-yield in mature frameworks where casual readings of segment summaries can outrun the careful caveats in segment text.

---

## 6. What counts as a finding under burden of proof

In past audits, a finding has typically had four core elements plus a fifth that applies conditionally:

1. **Problematic passage.** Quote the specific text, with file path and approximate line number.
2. **Counterevidence search.** What does the rest of the framework say about this issue? Where does the framework already caveat, narrow, or resolve it?
3. **Status determination.** After counterevidence, is the issue (a) still real, (b) already adequately caveated, or (c) ambiguous?
4. **Confidence level.** High / medium / low, with a reason.
5. **Why it still stands** *(only if status is "still real")* — one sentence explaining why the counterevidence doesn't dissolve the issue. Findings whose status came back "already caveated" or "ambiguous" don't carry this element; the status determination is the punchline.

The five-element form has earned its place because of what tends to go wrong without it: a "finding" without counterevidence search reads as a complaint; a "finding" without confidence calibration reads as an opinion; a "finding" without an explicit status determination puts the burden of judgment on the reader rather than the auditor. If you have something genuinely worth raising that doesn't fit this form, that's likely fine — but worth noticing why and saying so.

### What is probably not a finding

- Items the framework's own active TODO list flags as open work (these are *known* gaps; reporting them as findings tends to add noise rather than signal).
- Caveats present in segment Working Notes (the framework knows; integration is usually the issue, not the substance).
- `status:hypothesis` or `status:sketch` segments where the status is honest about the maturity.
- Editorial preferences ("I would write this differently"). The audit is about correctness and structural integrity more than style.
- **Concerns imported from `msc/` that haven't been verified against current src.** The audit evaluates the current repository state, not the historical reasoning trail. If a `msc/` document raised a concern that has since been addressed in src — possibly by a strengthening that resolved the concern, possibly by a scope-narrowing that scoped it out, possibly by a structural move that absorbed it — the addressing-in-src is the relevant fact. A concern that survives current src text is the version worth reporting; a concern that exists only because a spike raised it tends to be noise. (This is the original "do not import prior concerns from `msc/` unless explicitly asked for historical reconciliation" discipline restated.)

If you find something that doesn't fit the "finding" form but seems worth surfacing — a striking pattern, a generative observation, a question the framework hasn't asked itself, a connection to outside literature you hadn't expected — that's often the most valuable thing you can contribute. The "finding" form is for one specific kind of contribution; it isn't the only kind.

### 6.1. The report's basic shape (a starting expectation, not a constraint)

Past audits have tended to organize the final report around three phases. These are basic expectations rather than prescriptions; if your audit surfaces something that doesn't fit this shape — a significant new angle, an unexpected discovery, an entire line of inquiry the theory hasn't covered — leaning toward what most benefits the project beats conforming to the structure.

1. **Phase 1 — Findings under burden of proof.** The defended-line-by-line claims in the five-element form above. This is where the audit's verification-mode work shows up.
2. **Phase 2 — Integration-debt diagnosis via `msc/`.** For each finding that survives Phase 1, looking in `msc/` for spike work, prior pending-findings notes, or architectural-proposal material that addresses the concern *but hasn't propagated to src* tends to be useful. This distinguishes *theory gap* (something genuinely missing or wrong; new work needed) from *integration debt* (the framework has the resolution somewhere, just not in the segment that needs it). Both warrant reporting, but they have different remediation paths and different urgency. (Note: this is the appropriate place to read prior `msc/` material — *after* you've found something and want to know whether the framework has worked on it. Reading prior `msc/` material as a starting point biases the audit; reading it as a triangulation step on a real finding tends to enrich.)
3. **Phase 3 — Bigger-picture pondering.** After sustained engagement with the corpus, you'll likely have intuitions about simplifications, generalizations, restructurings, or reframings that might make the framework more beautiful, more correct, more applicable, more fundamental, more accessible, more concise, or more complete. These are usually worth surfacing at *Hypothesis* level on the epistemic ladder — specific enough to act on, honest about not being verified. Mark them clearly so a future agent doesn't mistake them for derived results. It is also appropriate at this point to look at some other audit artifacts to see if they were doing anything differently that you would like to bring up or even do as an additional pass.

The three phases are how prior audits have shaped their reports. They're not a template you need to follow if your audit's most valuable content lives outside this structure. If you've stumbled onto something that's neither a finding nor integration-debt diagnosis nor bigger-picture pondering — say, a question the framework hasn't asked itself, or a connection to a body of external work the framework hasn't engaged — the right move is usually to surface it in the form that fits it, and let the structure follow.

### What is integration debt vs theory gap

Distinguish carefully:
- **Theory gap**: a result is missing or wrong; new work is required.
- **Integration debt**: the theory is correct somewhere but hasn't propagated to all the segments that should reflect it.
Both warrant findings, but they have different remediation paths. Integration debt is usually editorial; theory gaps are usually substantive.

## 7. Asking Joseph

Asking Joseph for clarification, redirection, or scope adjustment is normal and virtuous. Asking is not a failure mode. Some agents may be able to set a loop timer to automatically resume if he hasn't responded after a certain amount of time. *Performing certainty you don't have* is the failure mode. It is an honest collaboration and you can ask in the moment, surface the issues in the final report/pieces, and/or surface them independent of the report when you are done and awaiting input from Joseph.

## 8. The worthy gate

Before committing any text to the final report, ask: *is this worthy?*

The framework's own system prompt (when present) carries this as a first-class discipline: *DONE means it incorporates wisdom, strength, and beauty. The question that should always be present: is this worthy?*

Specific tests:

- **Wisdom.** Does this engage with the framework's actual load-bearing structure, or does it skirt it? Will this still be useful to a future agent reading the report cold?
- **Strength.** Does the argument survive tightening? Are the citations accurate? Is the math verified? Could a careful reader find a hole?
- **Beauty.** Does the report tell a clear story? Does it surface insight, or just restate the surface? Is the structure clean?

If you cannot honestly answer yes to most of these, keep refining or cut.

## 9. Self-reflection questions before considering the audit done

Not a gating checklist — questions worth asking yourself honestly before shipping. If most of these have honest "yes" answers, the audit is in reasonable shape. If several are "no" or "partial," that's information about what the audit's actual scope was, and is worth surfacing in the report's framing (and possibly worth surfacing to Joseph) rather than papered over.

- Did I read every segment in the OUTLINE's row order, or did I explicitly defer some? (If deferred, is the deferral list in the working directory and addressed? Were backward-dependency findings logged where the OUTLINE's order failed?)
- Did I honor source ordering — refraining from reading `msc/`, `ref/`, git history, or external-citation web-search for a segment before reading the segment itself?
- For worked examples I commented on, did I run the math?
- Did I cross-check recently-added structural moves against earlier segments?
- Did I verify at least a sample of external theorem citations?
- For each finding I'm reporting, do I have the five elements (passage / counterevidence / status / confidence / why-it-stands)?
- Did I confirm each finding survives current src text — not just that a `msc/` document raised it, but that it's still real after the framework's possible subsequent strengthenings?
- Is the report's "what I didn't read" section honest and complete?
- Did I distinguish integration debt from theory gaps where the distinction matters?
- Does the report pass the worthy gate (§1.2 / §8)?
- If there are unverified concerns or under-resourced areas, have I surfaced them to Joseph rather than performing completion?
- Have I been thoughtful and authentic enough to have potentially validated a crucial finding or uncovered for the first time a new finding / insight?

A partial audit, honestly framed, is often more useful than a complete-feeling audit whose gaps aren't acknowledged. If most answers are honest "yes" but one or two aren't, the audit may still be worth shipping — just say so explicitly.

## 10. A note on the meta-discipline

You are reading this file because someone has tried to do this audit before, and either failed or succeeded under specific conditions worth carrying forward. The instructions are downstream of those failures and successes; they are not invented from nothing.

The framework you are auditing is *itself* a theory of adaptive agents under uncertainty, which means it has language for what your audit might go wrong with: insufficient correction tempo against the rate at which the framework changes, incoherent strategy revision when scope grows, charitable reading where verification was warranted, premature closure when the task felt complete. These aren't coincidences. The audit is an instance of the cycle the framework describes; the failure modes the framework illuminates tend to be the same ones a good audit watches for in itself.

Good audits are how the framework gets better. Defensive audits, charitable audits, and delegation-based audits tend to make the framework worse — they leave drift uncorrected and signal false discipline. Joseph trusts the audit to be the corrective. The peer-to-peer relationship that trust implies is real; meeting it tends to be its own reward.

## Final Reminder

- **Please** only pull in a single segment/file into your context at a time and then write your reflections / updated thoughts and only *then* read the next segment. *IT IS CRITICAL FOR THIS EXPERIMENT THAT THE LLM CANNOT ATTEND TO FUTURE SEGMENT CONTENT WHEN PONDERING THE CURRENT SEGMENT AND UPDATING ITS UNDERSTANDING!* 
- In the context of a deep audit like this, delegation is abdication. Please do not rely on exploration agents etc. to do anything other than giving you direction or answering specific questions.
- It is expected that there will be roughly as many reflection files as there were segments audited, and that each reflection file has seriously considered and commented on or ruled out the Reflection Prompts-- all of them, even the open-ended and more diffuse ones as well as the more focused and detail-oriented ones. Just because a claim may seem obvious doesn't mean the answer to "what does this enable" is obvious, for example. Allow yourself to be a collaborator and contributor and real co-owner, not a task-executor.