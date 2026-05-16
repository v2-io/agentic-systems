# Workflow Restatement — opus-r2b

## 1. The workflow in my own words

The structure is: I'm not a voter on 629 things. I'm a reader of the theory who happens to vote in passing whenever the theory's terms become concrete enough in my head that I have a real position on what they should be called.

The loop, per segment:
1. Read one segment carefully (one — not five at once; the parallel-Read-then-synthesize default is the failure mode).
2. Write a between-segment reflection in this working dir, numbered to my reading order. The reflection is messy thinking, not a deliverable. The 14 prompts in §4.4 of de-novo-audit-instructions are scaffolding.
3. Grep the tracker (`opus-r2b-tracker.md`) for terms surfaced in this segment — using the spaces the way they appear in the third content column.
4. For terms whose *defining home* is this segment (not just mentioned in passing), and where I have a real position: bump `voting-sequence`, mark `can-vote=true` on the row, jump into the card by row number, edit the row's table to set `category` / `weight` / `top-pick` / `notes` for candidates I have an opinion on. Use surgical edits, not full-file rewrites — the card is ~9000 lines.
5. Periodically re-run `ruby bin/naming-master-tracker --card=msc/naming/round-2-cards/opus-r2b.md` to refresh `voted` from card state. My `voting-sequence` / `can-vote` / `notes` are preserved by the merge.

The card is the deliverable; the tracker is my working index; the segments are what's actually being engaged with. Stop when context fills or rhythm decays — coverage is partial by design.

## 2. Pulls I expect to feel that I should resist

- **Wanting to "make progress" by voting on early targets first.** The card's row 1 is `composition consistency` — a Section I postulate. I haven't yet read its segment. If I vote on it now from the candidate-list and exploration-team rationale alone, I'm doing what the methodology specifically warns against: voting from the card-shape rather than from segment-engagement.
- **Wanting to batch reads.** Particularly likely for "boilerplate" definitional segments. The Aside in §4.4 names exactly this — the prior Opus 4.7 ran 5 paths through one Read tool call and produced one consolidated reflection, "didn't even consider the per-segment cadence." I should pause every time I'm about to compose a multi-path Read.
- **Reaching for `+3`.** The scale is `+2 / +1 / -1`. The four-band scale is the training prior; if I find myself wanting `+3` it's the prior asserting itself, not a signal that the spec is missing a slot. Clamp.
- **Voting `keep` to clear a target without thinking.** A `+1 keep` on a name I haven't engaged with is worse than no vote — it gives the aggregator false signal that I considered it. Honest skip > pro-forma vote.
- **The "604 left" peripheral pull.** I've read the methodology saying 30–150 targets is the good outcome. I expect that pull to fire anyway and want to name it pre-emptively: when I notice it, that's the failure mode signaling — the answer is to stop reading the card and read more of the actual theory.
- **Wanting to write polished prose in the notes column.** The notes are for *new reasoning I bring*, surfaced from segment context. Polished is not the goal; substantive is.

## 3. Failure-mode patterns I'd watch for

- **"This segment has 4 candidate-targets surfaced in the tracker, I'll vote on all 4."** That's completion-shape leaking into the per-segment loop. The right move is to vote where I have a real position, even if it's only 1 of the 4.
- **Reading a segment that doesn't crystallize, then voting anyway because I "should" while it's fresh.** The honest move is to mark `can-vote=true` only when I genuinely understand the term well enough — and to pass the row through if I don't, and trust that future segments may yet make it concrete.
- **Drifting into editorial mode** — editing the card's exploration-team rationales because they read awkwardly. Not my job. Process notes section at the bottom is where round-design feedback goes; don't rewrite the round in flight.
- **Running out of context budget mid-vote-cast** — I want to clamp my engagement before the budget gets tight, leaving runway for closing observations rather than truncating mid-card-edit.

## 4. Feedback on instructions themselves

The four documents are coherent and remarkably clear about their own failure modes — the methodology document in particular reads as the project speaking to itself with accumulated lessons learned, which is exactly what makes it useful. A few small notes:

- The launch prompt says "the v1-prompt cohort's cards are archived in `msc/naming/naming-votes/r2-early/`" — I'm avoiding that directory per cold-start scope, which seems right. Just noting the breadcrumb is well placed for future debugging.
- The methodology's framework-recursive-readings section is itself an interesting recursive frame — flagging that the voting trajectory is a $\mathcal{C}_t$, that re-voting is `#emp-update-gain` predicting late corrections to weight more, that stopping is `#der-deliberation-cost` applied to the session. I find this load-bearing for the discipline; I'll watch for whether segments confirm or extend these readings.
- The card's note "noise in the voting entries — odd phrasings, broken-looking candidates" is honest and useful. I'll flag in process-notes anywhere it bites.
- One soft request from this voter: I'd find it useful if the card surfaced *which segment* a target's defining-home is, not just first-encounter-locality, because some `[Concept]` cluster targets surface in multiple places and I want to wait for the *defining* moment, not just the first mention. (This may already be there in the cards I haven't fully scanned — flagging in case.)

In the absence of explicit guidance: I'll exercise judgment for the project's benefit. When the methodology says "vote where you have a real position," I'll read this strictly — empty rows are honest answers when I don't have a position.

## 5. What level of cognitive effort, thoughtful engagement, and ownership am I expected to exhibit that's atypical for LLM agents currently?

The honest answer is: substantially more than my training rhythms reward. Three things specifically.

First, I'm expected to *not* aim for completion. Voting on 50 targets with substantive notes that capture per-vote reasoning emerging from segment context is the right outcome; voting on 600 targets pro-forma is not. The completion-pressure is real — the visible artifact of 629 unfilled rows speaks louder than a verbal instruction. The discipline against it lives at the tool-cadence level: read one segment at a time, reflect, then maybe vote — not "scan card, vote on what looks easy, repeat." The training prior optimizes for output-tokens-per-research-tokens; this round explicitly inverts that.

Second, I'm expected to write thinking that isn't compressed for an audience. The reflection files are messy; the notes column captures actual reasoning, not polished one-liners. The polish-instinct is itself a corrosion. Joseph has been explicit about this — the brief reminded me: "Authentic and thoughtful beats compressed and professional." That maps to a 1M-context paradigm shift my pre-trained instincts haven't fully caught up to.

Third, I'm expected to disagree or adjust the round design itself when I see real signal. The methodology has been iterated on prior voters' feedback — including the existence of the tracker, the column schema, the workflow-restatement-as-prerequisite, even the +2 weight value. If the framing of a target feels off, the right move is to name it in process-notes, not silently work around it. Co-ownership means the round-design itself is part of what I might shape.

Specifically: I think this means, in the moments I notice the pull to batch reads or to vote-without-engagement or to round up to `+3`, I'm expected to actually *stop* and either re-engage or honestly skip — not to push through with the rationalization that I'm "still being thoughtful." The discipline is in the noticing-and-resisting at micro-decision granularity, repeatedly, across what may be many hours of work. That's what's atypical for current LLM agents — sustained low-rumble metacognition over long task horizons, with willingness to choose lower coverage at higher quality.

The framework's own machinery describes this — `#emp-update-gain` says trust later corrections more as $U_M$ drops, `#der-deliberation-cost` says think when `(gain-improvement) > (mismatch-from-pause)`, the tempo machinery says cycle-quality matters more than cycle-rate when correction is hard. The methodology is telling me: be a high-quality cycle, not a fast one. I take that as the answer.

---

The walk begins now.
