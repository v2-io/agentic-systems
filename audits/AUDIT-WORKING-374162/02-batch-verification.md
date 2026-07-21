# Batch-2 quiz verification

Checked the questions/answers against the five source files directly (`scope-agency`, `post-causal-structure`, `the-reality-model-intro`, `form-agent-model`, `form-information-bottleneck`), including their Working Notes / "Incidental audit gold" sections. Answered cold before reading the provided key, then compared.

## (a) Correctness against segment text

No factual errors found. Every answer's substantive content checks out against what the segments (body or Working Notes) actually say — I did not find a case where the key asserts something the corpus contradicts. The finding below is about *grounding*, not correctness.

## (b) The stated grounding policy is applied inconsistently — the batch-1 concern recurs, only partly fixed

The answer file's header states the corrective policy adopted after batch-1: *"answers are grounded in each segment's Formal Expression / Epistemic Status / Discussion; where an answer's full depth lives only in Working-Notes material, the core credit-line is body-derivable and the WN-depth is marked as bonus."* This policy is followed correctly in one clean instance and not followed in several others that need it just as much.

**Correctly marked (the policy working):**
- **A b02-2.4** — the Class-2/3 Markov-chain-failure content is explicitly tagged `(WN bonus)`. This is the model to generalize from.

**Not marked, though the content is WN-only (violates the stated policy):**
- **A b02-2.1** — the "asymmetry" clause (*"an agent with 100 nominal actions and 1 effective pair still qualifies... watch-item... downstream results must not quietly assume full contrast"*) is drawn verbatim from scope-agency's Working Notes §3 ("The existential quantifier is one effective action, not all"), not from the Formal Expression or Discussion. The body states the formal condition but never characterizes the asymmetry this way. Question b02-2.1 explicitly asks for it ("what asymmetry does it permit"), so a segment-only reader who nails the formal expression itself would still miss half the expected answer.
- **A b02-3.1** — the "structural availability vs exploitation" two-question framing is scope-agency's Working Notes §2 Candidate Discussion (attributed to Claude, AUDIT-WORKING-451729), not the segment's own Discussion. Nothing in the certified body of `scope-agency` distinguishes "has Level-2 access" from "exploits Level-2 access."
- **A b02-3.2** — the "boxed AI" instance is explicitly flagged in scope-agency's own Working Notes as *"Aspirational/normative reach pointing at the ELI volume, not this scope segment"* (under "Belongs elsewhere"). The segment's own author-side triage says this material does not belong to the segment's certified content, yet the answer key presents it as the worked example for a `[implications]` question without any bonus/WN flag.
- **A b02-3.4** — the entire nominal/nominal-coupling terminology collision is sourced from both segments' Working Notes, each explicitly labeling it *"a certified finding, routed via the findings track; recorded here for texture"* — i.e., a finding about the corpus's own inconsistency, not a settled piece of theory stated in either segment's Discussion. The question preamble ("a summary cannot supply it") signals awareness this is deep-reading content, which mitigates the concern somewhat, but it's still unmarked relative to the stated policy.
- **A b02-3.5** — both sub-answers are WN-sourced: (a) the generalist/specialist "mathematical root of expertise" point is form-information-bottleneck's "Belongs elsewhere" §92 (an aspirational field-contribution note, not Discussion); (b) the "crack in directed separation" framing is that same segment's "Belongs elsewhere" §93 ("Directed-separation tension (sharp, downstream)"). The body's own Discussion states policy-relativity and the π_cont device but never uses "directed separation" language or frames this as tension — that framing is WN synthesis.

None of this makes the answers *wrong* — the WN material is accurate synthesis of real corpus content — but it means the same measurement problem flagged in batch 1 (c) persists for roughly a third of this batch's questions (2.1, 3.1, 3.2, 3.4, 3.5), despite the header claiming the policy that should have caught it. A segment-only reader (Discussion + Formal Expression + Epistemic Status, no Working Notes) who fully comprehends the certified theory would score visibly lower than the key implies on exactly these five, through no comprehension gap on the theory itself.

Recommend either (1) actually applying the `(WN bonus)` tag to the five answers above to match the stated policy, or (2) deciding explicitly that Working-Notes-depth is in scope for this quiz series (a defensible choice, given the WN "incidental audit gold" is substantively part of these files) and dropping the policy claim from the header rather than leaving it half-true.

## (c) Sequential-comprehension design

No forward-knowledge leaks found. Forward pointers used (`#def-model-sufficiency`, `#result-structural-adaptation-necessity` in Ch.4, `#der-directed-separation`, `#deriv-strategy-cost-regret-bound`) are all named within the five segments themselves as pointers to *later* content, and questions ask what the segment says is coming, not what the later segment derives — consistent with batch 1's clean design. 2.3's "formulation ⇒ can't be exact" trap and 2.5's β-vs-ρ trap are well-aimed at genuine misreadings the segments explicitly warn against.

## (d) Discriminating power — self-experiment (answered cold first)

- **1.1, 2.5, 2.3** — strong traps; each hinges on a distinction the segment states explicitly but a skim would miss (binary-choice-insufficient; β-vs-ρ double-counting; formulation-choice vs exact-consequence).
- **2.6** — good discriminator; requires holding the full four-tier coupling taxonomy and correctly placing zero-coupling as adaptive-but-not-agency, which is easy to get half-right (e.g., placing it outside adaptive scope too).
- **3.6** — clean, well-grounded, no issues.
- **2.1, 3.1, 3.2, 3.4, 3.5** — as discussed in (b), these discriminate on Working-Notes depth as much as (or more than) on segment comprehension; a careful segment-only reader could legitimately score these differently than the key without a comprehension failure.

## Theory/framing observations beyond the quiz

Nothing to report — no issues spotted in the underlying segments themselves during this pass (the WN "Follow-up items" in `scope-agency` and `post-causal-structure` already self-report the two live certified findings — the Pearl-`do` depends-list gap and the nominal/nominal-coupling collision — so there's nothing new to surface there).

Staying available for follow-ups.
