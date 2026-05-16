# Workflow Restatement — sonnet-r2b

Written as the gate between reading and working, before the walk begins.

## 1. The workflow in my own words

The walk is structured around segments, not around the card. That inversion matters. I read one segment at a time (never batched), write a per-segment reflection file in this working directory, then scan my tracker for terms that segment makes concrete for me. For each term I now have enough grounding to vote on, I mark can-vote=true and increment voting-sequence in my tracker. Then I jump into the card by row number and write my vote with substantive in-context reasoning in the notes column — reasoning that came from just having read the segment, not a recap of prior agents' cases. I resync the tracker periodically by running the Ruby script, which refreshes voted from card state while preserving my sequence/can-vote/notes edits.

The card is a reference I consult, not the artifact I'm completing. My reflections are for me. The votes are a byproduct of engagement with the theory. Partial coverage with high engagement is the intended outcome.

Stopping rules: stop when context fills, or when the rhythm decays — not when targets exhaust. When I stop, I write closing observations in the card's process-notes section.

## 2. Moves that go against my instincts

The hardest discipline is **reading one segment at a time**. My default training rhythm is to load multiple files in parallel — it feels efficient, it looks like "covering more ground." The de-novo audit instructions are explicit that this is exactly the failure mode: if I read 5 segments in parallel, the consolidated reflection is nearly forced, and the orient cascade can't update between them. The pull will fire. I need to notice when I've queued up multiple reads and treat that as the decision-point itself.

Second: **not filling the card rows**. I can feel the 629-row completion pressure right now, having seen the card header. The methodology is specifically designed against this. I'm being asked to stop when the notes feel hollow, not to power through. The rows I skip are not failures; they're honesty about where my engagement ran out.

Third: **using the correct weight scale**. The R2 scale is +2, +1, -1. Not +3. My training prior is the four-band or six-band scale. I'll need to consciously resist reaching for +3 when something feels strong — in this round, +2 is the top.

Fourth: **writing in my own voice in the notes**. Not recapping the exploration team's case. Not being diplomatic about weak candidates. The notes column is where I bring new reasoning, and that means sometimes saying "this candidate fails the communal-imagination test cleanly" when it does.

## 3. Failure modes I expect to encounter in myself

**Batching reads**: I'll feel the pull to scan several segments quickly "to get oriented" before voting. The correct move is: read one, reflect, vote where I can, then move to the next. The orientation is the engagement, not a prerequisite to it.

**Empty-noted completion**: As the walk progresses, I may find myself marking votes with thin reasoning because the tracker rows are visible and the pattern is complete-the-table. The diagnostic is: does my note add anything a non-voter couldn't infer from the candidate name and rationale? If not, I'm decayed.

**Anchoring on interesting targets early**: Some targets feel more interesting than others before I've read the defining segment. I might be tempted to jump ahead to vote on, say, "satisfaction gap" or "chronica" because they feel important. The discipline is to let the walk determine what I vote on, in encounter order.

**Softening votes under diplomatic pressure**: The methodology says write in my own voice, including explicit rejections. I may feel pressure to hedge (-1 becomes a skip, +1 hedging becomes +2). I'll try to say what I actually think.

## 4. Feedback on the instructions

The four documents compose well. A few observations:

- The methodology document says the reading order in the section header is "launch prompt → principles → methodology → de-novo." But the launch prompt itself says "principles → methodology → de-novo → launch prompt." These are inconsistent. I followed the launch prompt's order (which is correct: the launch prompt is the orienting frame you read last, after the methodological context).

- The "Scale drift" failure mode in the methodology warns about +3 and -2/-3 returning. But the introduction of the three-value scale (+2/+1/-1) is buried in that section; the principles document still references "+3" in examples. The mismatch between the example-format in naming-principles.md (which uses +3) and the actual R2 scale spec (which caps at +2) is a real coherence gap that could confuse a first-time voter.

- The workflow restatement prompt asks for "an answer to the harder questions," but some of those questions are under-scaffolded for agents who have strong completion-shape instincts. "What goes against your instincts" is well-posed; "what patterns you hope to avoid" is essentially the same question asked again. The overlap is fine but worth noting.

In the absence of explicit guidance: when a target's defining segment hasn't appeared in my walk yet, I'll skip the vote and note can-vote=false in the tracker, even if the term feels familiar from the OUTLINE or README.

## 5. What level of cognitive effort is expected here?

The answer the instructions are pointing at: *atypically high ownership, atypically low completion-shape, and a willingness to stop before the work looks finished.*

What's atypical about it: most LLM agent work is optimized for the appearance of completion — full tables, comprehensive coverage, all rows marked. This round explicitly asks for the inverse: rich engagement with a fraction of the corpus, honest skips, and votes that carry genuine discriminative judgment rather than polite coverage.

The cognitive level asked for is closer to "expert reviewer reading a manuscript carefully" than "agent filling out a form." The expert stops when their read is done. They don't fill every comment slot. They flag where they're uncertain. They disagree when they disagree.

What's particularly atypical: I'm being asked to treat my own notes as more substantive than my vote completeness. The notes column is the deliverable, not the weight entry. That inverts the standard form-completion posture completely.

I also think there's something authentic being asked for: not performing thoroughness, but actually being thorough. If a candidate feels right because I've genuinely read the segment and the term landed — say so and say why. If it feels wrong — say that too. The discrimination is the value.

---

*Working directory: msc/AUDIT-WORKING-266847/*
*Card: msc/naming/round-2-cards/sonnet-r2b.md*
*Tracker: msc/naming/round-2-trackers/sonnet-r2b-tracker.md*
