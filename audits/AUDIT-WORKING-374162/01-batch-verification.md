# Batch-1 quiz verification

Checked the questions/answers against the five source files directly (INTRODUCTION.md + def-agent-environment, def-action-transition, def-observation-function, def-chronica, scope-adaptive-system), including their Working Notes sections. I ran each question cold before reading the provided answer, then compared.

## (a) Correctness against segment text

Everything checks out **except 1.2**, which has a real imprecision.

**1.2 — answer key is imprecise on the "known $h$" branch.** The question asks: if exactly one of $h$, $T$ is known exactly, what happens to the need for adaptation, treated separately. The segment (`def-action-transition`) only explicitly derives the *known-$T$* branch: "If $T$ were known, action selection would collapse to plain optimization over a known function." Nothing in the five segments derives a "known-$h$" branch the way the answer key states it. The answer key writes: *"Known $h$ + full-state access: no model maintenance needed, mismatch machinery vacuous"* — but this silently smuggles in "full-state access" as an extra condition the question never asked for, and it's not equivalent to "known $h$." $h$ is constitutively *lossy* (many-to-one, per `def-observation-function`); knowing the mapping $h$ exactly does not give you $\Omega_t$ back — you still can't invert a many-to-one function. So "known $h$" alone does **not** collapse to "no model maintenance needed." The honest answer, working from what's actually derivable in these five segments: with $h$ known but $T$ unknown, the agent's observations are as informative as $h$'s lossiness allows, but the environment still evolves unpredictably (unknown $T$), so the mismatch signal and model-maintenance machinery are still needed to track $\Omega_t$'s drift — adaptation persists, just without perceptual-model uncertainty compounding it. The answer key's framing effectively dodges the actually-asked case by substituting a different, stronger, undiscussed premise. Recommend either fixing the answer or narrowing the question to only the known-$T$ branch (which *is* cleanly supported).

Everything else (1.1, 1.3–1.6, 2.1–2.6, 3.1–3.6) matches the segment text and is a fair reading — including the trickier synthesis items (1.5 non-forkability, 2.6 fork-undetectability, 3.3 restoration, 3.4 passive-vs-agentic).

## (b) Sequential-comprehension design — no forward-knowledge leaks

No question requires material past `scope-adaptive-system` in the OUTLINE order. Forward-pointing slugs that appear (`#der-recursive-update` Constraint C3 in 2.4, `#form-agent-model` in 2.3/2.6, "Containment Dichotomy" in 3.2, "Level-2 causal contrast" in 3.4) are all *named within the five source segments themselves* as forward pointers — the questions ask what the segment says is coming, not what the later segment itself derives. 3.2 is explicit about this ("without having read their derivations"). This is clean design.

## (c) A structural pattern worth flagging: several answers are only fully grounded in the "Incidental audit gold" Working Notes, not the core Discussion/Formal Expression

This is the most substantive finding, and it cuts across the quiz-design goal itself. Each of the five segments carries a large appended "Incidental audit gold" Working Notes section — harvested commentary from prior de-novo audits, explicitly marked as candidate/not-yet-landed material (pedagogical framing, candidate Discussion additions, "follow-up items," etc.), distinct from the certified segment body.

Several answers draw their crispest, most-correct formulation from *that* appendix rather than from the core body:

- **1.5** (chronica vs $M_t$ forkability) — the core Discussion uses the loose word "state" for the non-forkable object, which the Working Notes themselves flag as a needed fix ("'Duplicating an agent's *state*' is loosely worded... A one-word editorial fix"). The answer key's crisp $M_t$/chronica distinction is the *proposed fix*, not yet the segment's actual wording.
- **2.2** (true entropy vs agent's belief) — this distinction is not stated anywhere in `scope-adaptive-system`'s Formal Expression, Epistemic Status, or Discussion. It appears only in the Working Notes as a "candidate Discussion point" ("The condition is evaluated from a God's-eye view, not the agent's... A candidate Discussion point distinguishing the modeler's predicate from the agent's belief").
- **2.6** (fork-undetectability from lossy $\phi$) — the core Discussion states $M_t=\phi(\mathcal C_t)$ is a compression; the actual derivation "two divergent chronicae can compress to the same $M_t$... an agent cannot always detect a fork occurred" is Working-Notes THREAD-E, explicitly flagged there as "§D-grade synthesis... a thread to verify lands at #scope-agent-identity" — i.e., not yet officially landed content.
- **2.5** (ordinal-not-metric, gap manifests in mismatch signal) — the core prose flags the property exists and says implications are "tracked in the Working Notes below," so this one is honestly sequenced (the segment itself tells the reader to look there) — less of a concern than the other three, but still means "read the segment" here means "read the Working Notes," not just the Discussion.

None of these are *wrong* — the synthesis is sound and the Working Notes are part of the same file — but it means the quiz, as constructed, partly tests "did you read the full file including 40+ lines of appended audit commentary per segment" rather than "did you comprehend the core theory claims." That may be exactly what you want (arguably that IS the deeper-comprehension test, and a summary-fed reader is even less likely to have absorbed the Working Notes than the Discussion), but it's worth being deliberate about, since it changes what "sequential comprehension" is measuring — a reader who nails the Formal Expression / Discussion cold but skipped the Working Notes appendix would miss 1.5, 2.2, and 2.6 despite genuinely understanding the segment's canonical claims. Flagging so you can decide if that's the intended bar or if it's worth either (a) noting explicitly in the quiz preamble that Working Notes are in scope, or (b) reweighting/relabeling those three as "deep" bonus questions rather than core comprehension checks.

## (d) Discriminating power — self-experiment

I answered cold before reading the key. The questions that would most reliably catch a summary-fed reader:

- **1.1** — very effective trap; "simplifying assumption" is the natural wrong answer and is explicitly named as such in the answer key's grading note.
- **1.4** — effective trap; the "true" half of the claim reads plausible on a skim and the falseness hinges on the umbrella/tier distinction, which is easy to miss without reading `def-agent-environment`'s Discussion carefully.
- **2.3** — good discriminator; the $a_{t-1}$ argument is exactly the kind of detail a summary drops.
- **2.5** — good trap; "wall-clock time" is the natural (wrong) assumption.
- **1.2, 2.2, 2.6** — as noted in (c), these test Working-Notes-level depth rather than segment-level comprehension; a very careful segment-only reader could reasonably miss them without that meaning they didn't comprehend the segment.

No question struck me as too easy / summary-passable.

## No issues found with the theory framing itself in this batch (nothing to report under "if you spot anything off").

Staying available for follow-ups.
