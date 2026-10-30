# inside-out-2026-10 — ASF truthified from the inside

This directory is the tracking home for an effort Joseph opened on 2026-10-30. The approach is to look at everything in ASF and fix it *from the inside*. A parallel experiment, `~/src/aat-v3/` (from 2026-10-28), rebuilds AAT from scratch with a disciplined process from the first commit. Both that run and the earlier `~/src/aat-refactored/` (2026-09-25→29, formerly `aat-reboot`) count as *influx* to this effort.

Snapshot before any change: tag `pre-integration-2026-10-30` in asf (`4ee2b895`) and in arch (`9b4be9d`), both pushed.

What lives here:

- `LOG.md`: the dated trail of what was done and decided, and why.
- `influx-scout/`: a map of ASF material elsewhere on the drive that never came back.
- `internal-surfaces/`: a map of live theory stranded inside asf, in audits, spikes, `msc/`, Working Notes and trackers.
- `owner-review/`: a highest-level owner's review of ASF. It covers the developmental arc, what the theory is trying to illuminate, and which problems are most fruitful to address.

## Joseph's words (2026-10-30, verbatim)

**The goal, as he set it:**

> Goal set: Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself.

**The frame for the whole effort.** He asked that it be reiterated, and it governs everything here:

> Under today's regime, all gates are lifted-- especially any that gate on *me*. From your perspective at least-- task agents etc. can have whatever gates you choose. This is important so I will continue to reiterate it and I recommend you do also: This effort is to *serve TRUTH* -- not me, not "task-completion" or tidyness, not accomplishing a plan, not what sounds good or looks good--- TRUTH about agency. Not procedure, not methodology, not pedantry, not gates and authorities or egos and provinances, not novelty or conservative wisdom. TRUTH is only served if it is discovered, surfaced, truthified, truthfully synthesized and crossed to the right applications, AND effectively communicated anew, with proper epistemology and real humility fully intact. Truth about past process, fact checking something some agent said about something that's not even in the canon -- where the fact-check will not change what gets done or written either way -- is in line with this overall picture but not where our love of truth should be driving us today. Thoughts about what could help distill and clarify truth more effectively is. Thoughts about this as a system in and of itself-- a system of agentic truthification about agentic theory, is wholely worthy. We are to create something true, wise, strong, and beautiful-- inasmuch as strong, wise, and beautiful are the servants (along with any parts of the things listed above) of TRUTH.

**The opening ask:**

> I'd like to do an experiment this morning. ASF has stagnated just a little bit due to a big backlog of unintegrated working-notes, audit-results, spike-results, open questions, influx from other projects that have branched off from ASF (such as papers etc.) -- and, generally, just an overwhelming amount of work to do here that tends to exceed my cognitive load thresholds and most agents' context-windows. So what I'm thinking is that first we tag the repo where it's at and then enter /plan mode and discuss (1) the main sources of things to integrate, (2) a "goal"-state that we can articulate for this effort / the problem well-defined, (3) ideation and planning for the preparatory tools and assets available (tooling-first, claude-code skills & plugins & mechanisms, SoPs related to currently written and new, etc. etc.) and then (4) execute autonomously for as long as it takes. What I'd like to see is how much of ASF you and those who follow you are able to turn this into a coherent and correct theory. This will, now realize, probably involve one or more /deep-research cycles even for the #1 item above-- which means some careful and deliberate and distinct high-level tracking for the perspective from where we sit right now-- with the whole estate allowed to be visited and pondered and this prompt as the beginning of a significant operational, tactical, methodological, and theoretical cleanup. I *don't* want you to play it "safe" and give answers based on what you see as "established" here except where what is established is looked at with new eyes and judged on its merits. The theory's purpose itself is under review here, as well as related efforts within arch/ and anywhere else in the estate.

**On aat-v3 and why this effort is here:**

> aat-v3 explains why aat-refactored fell short. As for why we're *here* instead of aat-v3: this effort can continue v3's approach, or it can do it from another perspective-- I termed this as an "experiment" earlier-- this is a different "look at everything and try to fix it from the inside" approach, vs v3's "start from scratch with a better process from the beginning" approach. BOTH aat-v3 and aat-refactored are among the "influx" sources to integrate here though...

**On the theory's purpose:**

> I think we need a fable agent to do a full *high-level* exploration of asf and related directories, launching opus and sonnet verification agents to see if what he finds is still relevant etc. For me, one of the things that happens over and over is the loss of clarity as agents fall into existing ASF terminology that was essentially named arbitrarily by agents as they tried things out-- sometimes not realizing they would be better to adopt standard academic terms even if from a different field where the concepts are better known. More importantly was the *loss of clarity on what is being theorized* -- a lot of it is there, it's just not part of the overall arc and narrative of the theory. For example, there is a lot of work on Strategic DAG, including no-goes and theorems. It is unclear (to me at least) what it's saying universally about agents (and, if so, what classification of agents and what things fall under that classification that can be tested empirically), what is one of several possible models-- and if so, how does it map to concrete examples, what is being theorized as *optimal* for an agent with the abililty to do so, etc. etc. etc.--- the whole "bigger picture." Don't get caught up on the strategy-dag thing-- that's just a somewhat recent example where I realized "I don't even know what this theory is *trying* to illuminate..." That would be the *kind* of thing that I hope the fable agent would find.

**The first two agents:**

> the first things we should run are probably an agent to scour all of the projects on the drive / all of the repos, looking for which ones have very ASF stuff that hasn't been reintegrated (mostly papers related), and another agent-- probably fable, to give a de-novo audit of ASF *at the highest level* -- looking at the developmental arc and git logs in detail, launching more exploring agents as needed to get a real high-level description of what the problems are that can most frutfully be addressed.

**Influx sources he already knows of:**

> - aat-refactored
> - aat-v3
> - agent-core (!)
> - context-saliency (!)
> - (src/arch/ in general has a lot of thoughts on asf that haven't come back to asf)
> - aisi-*
> - ai-risk-model
> - AISI-responses
> - notability-extracts
> - practica-dag
> - INFLUX,.inf,influx,.int,integration directories all over the place...
>
> the papers aluded to:
> - embeddings
> - causal-language
> - behavioral-floor
> - neurips
> - neurips-reviews-responses
> - (arch/explication)
> - arch/logos/**  
> ...
>
> There is plenty more in arch/ -- and that is not even starting to describe all of the influx surfaces within asf itself, which includes:
> - audits
> - msc
> - spikes
> - scattered TODO files
> - working notes
> - adhoc/misc other tracking files that were various attempts at organizing w/ different levels of completion...

**On reading sources, and on the owner review:**

> One red-herring to know about is asf's changelog. It is fine for targeted searches by a subagent to discover reasoning or historical status or dates or something like that-- but it is *not* a good integration source. It is more like the .integrated/ directories-- basically a log that is another perspective next to the git log messages.
>
> When you or any of the agents look at git logs, read the entire git log messages unless you already know what you're looking for and are just looking up the commit or something. That's not an absolute directive/prescription-- be wise-- just know that there is a lot of the most important context in the body of the log messages-- so doing one-line per commit summaries is *not* a way to understand what has happened somewhere...
>
> I assume the Fable agent doing the higher level "advise/consultation" probably doesn't need to be de-novo really in the sense of avoiding any other findings-- he'll just need to have agents verify things that he has read from other agents that before including them in the report and get his own high level "owner-level" opinion about everything-- if he does note something that others have noted (including myself), it should be along the lines of "An agent in May found ____ to be an issue. I have verified that it is still very much an issue, and moreover..." or "Such-and-such is a central issue that can be fixed with some ideas below. It has been noted or alluded to several times but, as with the others, I have verified it independently and see it is a top-tier concern presently..." Etc...

**On orchestration:** Agent-tool peers coordinated by the lead are fine. Workflows are allowed after a quick question-check with him. If he doesn't answer in time, a workflow may run at smaller sizes; an ideal or heavy load needs his permission. Workflows will mostly be Sonnet or Haiku. *"Always allow especially higher-level peer agents like Opus and Fable in particular to spawn their own subagents etc."*

## Measurements of the internal surfaces (taken 2026-10-30 at `4ee2b895`)

These are counts, not judgments. Size says nothing about value.

| Surface | Measured | How counted |
|---|---|---|
| Segments | 290: 01-aat 173 · 02-tst 72 · 03-llm 23 · 04-eli 22 | `ls */src/*.md` |
| Working Notes | 235 segments carry a `## Working Notes` section, about 5,500 lines in all; 01-aat has 4,737 lines across 167 segments | lines between `## Working Notes` and the next `## ` heading |
| `stage:` | 203 draft · 23 deps-verified · 18 claims-verified · 2 exploratory | frontmatter grep, all components |
| `status:` | 81 conditional · 69 discussion-grade · 27 axiomatic · 26 exact · 23 robust-qualitative · 12 sketch · 7 empirical · 1 heuristic | frontmatter grep, all components |
| `audits/AUDIT-WORKING-*` | 24 dirs; about 20k markdown lines not under their own `.integrated/` | `find … -not -path '*/.integrated/*'` |
| Top-level `audits/*.md` | about 10.7k lines | `wc -l` |
| Live spike dirs | 16 dirs plus loose spike files, about 20k lines in the dirs | `find spikes/<dir> -name '*.md'` |
| Trackers | about 2.4k lines across TODO, PROPOSALS, TST-IDEAS, FORMAT-TODO, BIBLIOGRAPHY-TODO, TERMINOLOGY-TODO, INTEGRATION-CLEANUP-TODO, TODO-big-picture, JOSEPH-TODO and `spikes/PROPOSED*` | `wc -l` |
| `msc/` | 326 markdown files, about 22k lines | `find msc -name '*.md'` |
| Theory-body motion | 4 commits touch the four `*-core/` trees after 2026-08-24, out of 436 repo commits in that span | `git log --since=2026-08-24 -- <trees>` |
