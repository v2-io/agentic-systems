# Workflow Restatement

Agent id: `codex-r2b`

## My Working Model Of The Round

This is not a card-completion exercise. The useful output is a trail of engaged first-hand reading that produces votes only where I have enough context to make an honest judgment. The card is the durable voting surface; the tracker is my index and state ledger; the segment walk is the thing that gives the votes substance.

My rhythm will be:

1. Orient from the approved top-level material, then write falsifiable initial predictions before reading any source segment in detail.
2. Walk the canonical OUTLINE order, one segment at a time. Before reading a segment, check its `depends:` frontmatter against what I have already read. Appendix proof back-pointers can be followed immediately; other downstream dependencies should be recorded as ordering trouble rather than silently repaired.
3. After each segment, write a numbered reflection in this directory while the segment is still the live object in context. The reflection should record what changed in my model, what naming questions surfaced, and what future errors to watch for. It is not meant to be polished.
4. Scan `msc/naming/round-2-trackers/codex-r2b-tracker.md` for terms or concepts that the segment actually made concrete. If a segment merely mentions a term, I should usually wait for the defining home.
5. When I now have a real position, mark `voting-sequence` and `can-vote=true` in the tracker, then edit the matching target in `msc/naming/round-2-cards/codex-r2b.md`. The card vote uses `category`, `weight`, optional `top-pick?`, and notes. Notes should contain my own segment-grounded reasoning, not a paraphrase of the exploration team's case.
6. Periodically run `ruby bin/naming-master-tracker --card=msc/naming/round-2-cards/codex-r2b.md` so `voted` reflects the card while preserving my tracker notes and sequence fields.

The card preamble settles the Round 2 mechanics for this agent: weights are `+2`, `+1`, and `-1`, not the older `+3` scale shown in some examples. I will use `+2` for strong preference, `+1` for acceptable or mild preference, and `-1` for explicit rejection. Absence stays absence, not neutrality.

Stopping is not "all 629 targets." The honest stopping rule is context pressure or rhythm decay. Before stopping I should add process/cold-start observations to the bottom of the card if anything about the target framing, candidate noise, instructions, or method deserves to be preserved for the round designers.

## Instincts I Need To Watch

My default coding-agent reflex is to gather lots of context quickly, parallelize reads, and synthesize. That is exactly the wrong shape for the segment walk. The method depends on the model update after each single segment; batching source segments would turn the reflections into retrospective summary instead of incremental cognition.

I also expect a pull toward visible progress: more rows voted, more tracker entries marked, more files read. For this task, that can degrade the signal. A sparse card with real notes is more useful than broad coverage generated from naming heuristics.

Another reflex is to resolve ambiguity too quickly by using local names as if their meaning were obvious. Many targets on the card are terms whose first encounter is not their definition. I need to distinguish "this phrase appeared" from "this segment made the thing enough of a thing that I can judge its name."

The voting scale is a specific trap. The principles document still contains older examples with `+3`; the methodology explicitly names scale drift as a prior failure mode, and the card uses `+2/+1/-1`. If I reach for stronger gradations, I should translate that conviction into notes and the top-pick marker, not invent weights.

Finally, I should not treat the exploration-team rationales as a substitute for my own judgment. They are candidate context, not authorities. If a candidate sounds strong in the rationale but the segment makes it feel inflated, noisy, or misframed, I should vote or note accordingly.

## Failure Patterns To Avoid

The main failure would be card traversal disguised as engaged voting: scanning target after target, using first-impression aesthetics, and filling rows because empty rows look like unfinished work. I will keep the segment as the anchor and use the tracker only after a segment surfaces terms.

A second failure would be reading ahead for convenience. I should not open multiple source segments at once, and I should avoid historical or working artifacts before the relevant segment has had its first encounter. The launch prompt narrows this for naming: inside `msc/naming/`, I may read only the whitelisted round-design and my own card/tracker materials; I must not read other voters' cards, trackers, votes, aggregates, or prior-round vote-shaped artifacts.

A third failure would be pro-forma reflection. If a reflection could have been written from the filename and the card locality sentence, it has not done its job. The useful reflection names how the segment changed the available vocabulary, what it made concrete, and what it left unstable.

A fourth failure would be sticking with an early vote after later segments improve my understanding. Updating or removing my own vote is part of the method, not a defect. If that happens, I should make the trajectory visible through tracker sequence/notes or card notes where useful.

## Instruction Feedback And Local Decisions

There is a real but manageable conflict across the documents about orientation material and weight scale. The de-novo audit document tells auditors to read `README-auditor.md` and avoid `README.md`; the Round 2 launch prompt says naming voters may read `README.md` directly because priming on the actual project concepts is useful. I will follow the launch prompt for this naming round and read `README.md`, while still preserving the one-segment-at-a-time discipline for source segments.

The principles document's "What to return" section describes a Round 1-style `msc/naming/naming-votes/{agent-id}.md` output and `+3` examples. The Round 2 launch prompt and the actual `codex-r2b` card supersede that for this task: I will vote directly in `msc/naming/round-2-cards/codex-r2b.md`, keep state in `msc/naming/round-2-trackers/codex-r2b-tracker.md`, and use the card's `+2/+1/-1` scale.

I have not read any excluded `msc/naming/` artifacts in this session. I have read only the launch prompt, the three instruction docs, my own card preamble, and my own tracker.

## Expected Level Of Effort And Ownership

The expected effort is atypical for an LLM agent because it asks me to resist the training-shaped path of quick synthesis, confident completion, and broad shallow coverage. I am expected to behave less like an answer generator and more like a collaborator leaving a trustworthy cognitive trace: make first-hand judgments, record uncertainty, notice when the instructions themselves have bugs, update my position when later evidence changes the read, and stop before the work becomes hollow.

The ownership standard is that my votes should be defensible to a future reader with 100% context turnover. If I vote to keep or rename a term, the note should show why the name will or will not help a skilled reader six months later. If I skip a target, that is legitimate; if I fill it without understanding, that actively harms the aggregation. The work is valuable only insofar as it preserves independent judgment under a method designed to keep that judgment from collapsing into completion pressure.
