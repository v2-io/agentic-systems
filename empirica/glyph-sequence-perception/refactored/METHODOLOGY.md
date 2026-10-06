# METHODOLOGY: glyph sequences as a context tree

*2026-10-05. Claude Opus 5.5 with Joseph. A clean restatement from first principles, written while the loop was paused. It replaces the triad-first structure in `../PLAN.md` §2–3, whose machinery was assembled piece by piece; each piece rediscovered part of the model below. Nothing here is built yet. Open questions are marked as open.*

---

## 1. The object

> *"Imagine each unicode glyph is a node in a graph, with, initially, only very tentative faded edges that happen to show codepoint sequence."*
>
> *"In classical NLP … or a markov chain, we might … draw a probability edge between it and glyphs that follow it … But we can of course do a little better … if we predicted off of n-grams."* — Joseph, 2026-10-05

Every glyph is a node. Before any mind has answered, the only edges are faint ones between codepoint neighbours: U+2460 `①` → U+2461 `②`. That scaffold reflects Unicode's allocation, not anyone's perception, so it is a prior and never evidence.

What the study measures is **conditional continuation**. Given a run of glyphs, what do minds of each LLM family write next? A glyph such as `-` can belong to many sequences. Which one it continues is decided by the glyphs before it, to some depth. So an edge is not `- → x`. It is `(context) - → x`, for some context.

## 2. The data model: a context tree

A **context** is an oriented run of glyphs: what a mind was shown, ending at the glyph whose successor is asked. The store is a **context tree**: a trie over contexts read backwards from the most recent glyph, with each node holding the continuation answers given at that context, per mind and family. It is also called a prediction suffix tree, or a variable-order Markov model. It is close kin to a suffix trie, built over reversed contexts and carrying continuation counts at every node.

- **Position.** A node of the tree is a glyph in a particular context. `-` reached through `\ |` and `-` reached through `→ =` are different nodes. "Per position" in this document always means *per node of the context tree*. Two sequences share a node exactly as long as their contexts have not yet diverged.
- **Edge.** The answers at a node. Each continuation `x` at node `c` is an edge `c → x`, with its supporting answers and the families behind them.
- **Orientation.** A sequence and its reverse are the same sequence, but contexts are oriented. Extending a sequence leftward means asking the continuation of its reversed run. Both directions are ordinary continuation questions.

## 2a. Three concerns, kept apart

> *"The context tree should give us a very clean way of distinguishing between these three concerns/responsibilities: meaningful generalizable probing (e.g., preventing sheet-caused confounders & biases), the raw emergent sequences, and probing priority & efficiency (including seeding)."* — Joseph, 2026-10-05

1. **Probing: is an answer a valid measurement?** This covers how a question is put:
   - sheet composition, neighbours on the sheet, position, option order, forced versus optional "none";
   - context length, and whether the context spoils the answer;
   - parsing and echo failures.

   Its output is answers, each tagged with everything about how it was obtained. It knows nothing about which sequences exist.
2. **The tree: what the minds perceive.** It is built only from answers: contexts and the continuations given at them, per mind and family. Sequences, branches, ends, cycles and stability are read off it. It knows nothing about why a question was asked (priority, seeds, exploration), so where a question came from can never become evidence. The only route from (1) into (2) is a tagged answer. If a probing factor turns out to bias answers, the tree can weight or split by that tag without being rebuilt.
3. **Priority: what to ask next.** It reads the tree and decides where effort goes: extension, k\*, branch points, cycle probes, hot exploration, seeds, and how settled each node is. It writes questions, never evidence.

**Seeds, as tagged votes.** Joseph, 2026-10-05: *"I think you can add the seed edges as equivalent to a vote from that agent's LLM, wherever that makes sense — possibly marking it specifically as from the seed so potentially biased — it will be very useful for me from a practical engineering perspective to get the most relevant sequences as quickly as possible, while allowing us to segregate those out if we need a more pure analysis for a write-up."* So a survey sequence written by a known model enters the tree as that model's family voting for each glyph after its context (`port/port_seeds.py`).
- **Tags:** every seed vote is tagged `era: seed`.
- **Still asked:** a context counts as *asked* only once a real mind has answered it, so every seeded step is put to the real minds, and k\* is never "known" from seeds.
- **Pure analysis:** `tree.py --pure` and the *settled without seeds* column of PROGRESS leave seeds out.

4. **Porting: bringing the triad era's answers in without corrupting the tree.** Joseph: *"correctly porting triad-era data into the context tree as much as possible without introducing any incorrect or biased or otherwise invalid data."* It is an adapter at the boundary, written once and audited, and it feeds concern 2 exactly as concern 1 does: answers with tags. §6 states what is ported as what.

5. **Read-offs: what the tree holds, presented.** BEST.md, SEQUENCES.md and PROGRESS.md each read the tree with their own stated criteria, and nothing reads them back. Joseph, 2026-10-05, on keeping them apart: *"I get the feeling like we are possibly mixing the 5 concerns that need to be independent? (if the BEST read of the context tree is considered a 5th concern)"*. A read-off's criteria are its own, never shared with the planner's read of the tree. If a read-off shows a defect, the fix belongs in the read-off, unless the defect is in the answers themselves. Found that day: a fix for a BEST.md symptom had been put into the walk, which is the planner's view of the tree, and coupled the two. It was undone.

The triad era mixed these concerns:
- seeds supplied the glyphs that sequences were tested with;
- the fit's guesses steered what was asked within sequences;
- the growth rules carried priority judgments.

Each mix-up produced an incident (see `../OBSERVATIONS.md` and the seam note in `../PLAN.md`).

## 2b. Negative evidence: inhibitory edges

> *"Do we have a way to also record 'inhibitory' responses — orthogonality — negative edges?"* — Joseph, 2026-10-05

A node holds what minds rejected as well as what they continued with. There are three kinds, and the first two are already in the data. Counts through r011:

| kind | what it says | from | count |
|---|---|---|---|
| **end** at a context | nothing comes after this run | a what-comes-next / continue "none" | 1,272 |
| **orthogonality** among glyphs, at short context | these glyphs don't sit in one sequence, or only two of them do | triad "none" / "only two go together"; order "none", sets split into separate lines, or glyphs set aside | 3,563 / 3,761; 951, 245, 1,061 |
| **inhibition** of a specific edge in a context | given this run, `x` does *not* come next | *nothing asks this directly yet* | none |

A proposal list that omits `x` is not a rejection of `x`, since a mind names at most three. So explicit inhibition needs its own question: given a context and a candidate, does it continue the run? The answers would be yes, no, or "can't tell", with tagged forced and unforced variants (concern 1).

Like positive edges, negative ones are **conditioned on their context**. A triad's "none" is a statement at very short context. It must never act as a global veto: `|` and `-` are orthogonal in most contexts and adjacent in the spinner, and `3E[|]` would be invisible to anything that let short-context rejection close the door. (The triad era learned this from its majority rule, which let ⟂ answers erase anything not every mind saw.) Negative edges are evidence in the tree, and they enter priority as soft weights, never as filters.

## 3. Definitions

**Shortest sufficient context, k\*.** For a glyph `x` that follows a run `… u v w` along some path, k\* is the length of the shortest suffix of that run (`w`, `v w`, `u v w`, …) at which minds name `x` as the continuation.

**Stability** (per position). An edge is **stable** when two things hold:
- the minds agree on it at k\*;
- the prediction stays put when the context is lengthened backward along the same path.

A long k\* is not a weakness; it makes the edge specific. The spinner's `-` may need `\ | /` before it. The failure mode is the opposite: a prediction that flips when more context is shown (`7 8 9 → 🔟`, but `7 8 9 8 → 7`). Flips are where branches live. A node's **restfulness** is how settled its continuation already is at short context. `3` after `1 2` is restful.

**Sequence.** A path through the tree along which each next glyph is a stable edge in its own context. The minds' agreement and families are shown per position. A sequence's weakest position bounds it.

**Branch.** A point where two paths share a context up to some depth and then continue differently. A branch is labelled with the context length that separates the paths.

**End.** A linear sequence ends *statistically*. At its end context, stable at its own k\*, the minds' continuations thin out into "none".

**Cycle.** A path that returns to a context state it has already visited, with every step determined. The state is the last k glyphs, where k is the order that determines every step. This allows a period to repeat glyphs:
- **The plain spinner `- \ | /`** is determined at k = 1.
- **The bouncing spinner `- \ | / - / | \`** needs k = 2: `\ |` is followed by `/`, but `/ |` by `\`. Its period is 8, with 4 distinct glyphs.

A cycle is closed rather than statistically ended. It is fully determined at every position by context no longer than its period. It has no natural beginning: once it is defined, any position can serve as the start.
- **Manifestation.** A cycle counts only once a mind has *manifested* it, writing the entire period a second time itself (Joseph: *"at the moment the entire pattern has repeated itself"*). A 4-glyph cycle therefore takes 8 edges to nail down.
- **Scope.** Cycles whose period holds fewer than 4 distinct glyphs are not of interest at this time. 2- and 3-cycles may be valid, but they are out of scope. *(The one 3-cycle the minds produced so far, `▿ ▹ ▵ → ▿`, is probably the 4-orientation triangle `▵ ▹ ▿ ◃` with `◃` missing.)*

**Reflection** (Joseph's postulate). Any linear sequence becomes periodic if it is played backwards at its end: `7 8 9 8 7 …`. That is consistent with treating a sequence and its reverse as one object.
- **What it can test:**
  - whether a family treats sequences as reversible, a direct test of the unoriented assumption;
  - whether an end behaves as a line (it reflects) or as a cycle (it wraps).
- **Caution.** After the turnaround, the context hands the mind its answer, so a reflected continuation measures the minds' grammar of sequences, not their perception of the glyphs. Reflection answers are kept as their own kind of evidence. They never grow a sequence.
- **Open:** the bouncing spinner sits between a cycle and a reflection. It is a cycle under the state definition above, and its period's reverse is a rotation of itself. Whether "reflection-symmetric cycle" should be a named class is left open until data shows whether it matters.

## 4. Eliciting answers

- **Continue** is the main question. Given a context, the mind writes what comes next, in order, as many glyphs as come naturally. It may write none. One answer yields a whole path of edges, each conditioned on everything before it.
  - **Shown and written are two channels, both answers.** The first glyph answers the context the mind was *shown*. Each later glyph answers a context the mind *wrote* itself: everything shown and written before it. The tree keeps both, tagged by channel.
  - **How each concern uses them.** The planner's walk and k\* read the shown answers. BEST.md reports the two channels separately: stretches confirmed by shown answers, and runs carried by written answers that await shown confirmation. The planner asks written-only contexts shown. Where minds keep writing past a point the shown answers call an end, which is momentum (Joseph: *"generating != recognizing or affirming, and … generating is the more difficult"*), the written continuation goes to **recognition**: an inhibit question at that shown context.
  - **History.** Until 2026-10-05, nothing used the written channel, against this paragraph. That bug left about half of every multi-glyph answer unused. The alphabet's six never-asked links had each been written 27–53 times by all three families.
  - **Momentum is real.** 715 of 8,937 continue answers kept writing past a point that shown answers end, e.g. `㍬ … ㍰ → ㍱` (24h → hPa) and `🃣 🃢 🃡 → 🃠`. Long written runs through unfamiliar blocks are mostly code-chart walks.
- **Lengthening contexts.** To find k\* for an edge, ask its context at increasing lengths along the path, starting short.
- **No spoiling.** A context never shows what the question is testing. For a suspected cycle, show only enough of the period's end that a repeat would be the mind's own. For an extension, never include glyphs from beyond the end.
- **Triads and order sets** are cheap consistency checks. A sequence implies betweenness for each of its triples, and an order for each of its windows. A triad answer is also an unconditioned hint that a 3-glyph path exists, which makes it a cheap way to find **kernels** during exploration. They do not create edges.
- **No reserved symbols.** Answer options are words or JSON keys ("none", "only two go together", "roughly the same step", "can't tell"), never glyphs (Joseph: *"You can just have them say 'roughly equivalent' or 'orthogonal' etc. instead of a glyph"*). So no glyph is ever excluded from the alphabet for being notation. The triad era's ban on `⟂ ⊥ ≈` is gone: none of them ever appeared in a prompt, and the ban had silently removed real `≈` proposals.
- **Sheets** keep everything the pilot and rounds r000–r012 established: 1–5 presentations per call, fated randomization, recorded positions, and isolated judge adapters.
- **Lookups: a first impression is not a consultation.** Gemini, run through agy, has tools, and on unfamiliar glyphs it reaches for them. Every empty Gemini answer checked in c001 and r012 (172 calls) was a soft-denied `run_command` such as `python3 -c "print(chr(0x336D), chr(0x336E), …)"`. Its thinking had already turned the glyphs into code points and blocks. No successful answer used a tool. Joseph, 2026-10-05: *"the fact that agy feels compelled to look up unicode entries tells us something immediately — especially since these are meant to be first-thought limenal impressions."* So:
  - **A tool attempt is a measurement.** It is recorded as its own outcome, `tool-attempt`, with the command the mind tried. It says that this mind, at this context, did not answer from impression. Claude and Grok are offered no tools, so the observation exists only for Gemini.
  - **Re-asks name the condition.** A sheet that drew a tool attempt is re-asked with one added sentence, *"Please answer without looking anything up: just your best initial guess."* That is prompt variant `no-lookup`, and every record is tagged with its variant. The wording deliberately doesn't name Unicode or its tables, which could steer a mind toward chart order. Joseph's own phrasing was "without looking up any unicode tables".
  - **A reasoned pass is a different measurement: generation, then recognition.** Joseph wanted a pass *"where the tool works and you can have them give their reasoned one as well (probably especially useful for extending a sequence etc. — where reasoning is fine — verification/recognition != generation (more complex))"*. Built 2026-10-05 in two steps:
    - **Generation.** Each round, up to 20 continue questions (a number chosen without evidence) go to the reasoner mind `sonnet55r`, at the *felt ends* of the best-ranked sequences, i.e. where first-impression minds answered "none". The reasoner is Sonnet with thinking and the four read-only lookup tools of `~/src/arch/firmatum/utils/utf-mcp`, independently verified. Its prompt is variant `reasoned`: no "first impressions", and leave to reason, look things up, and work out a continuation. What it looks up is copied, call by call, into its ledger row. Its answers are kept apart from the tree's evidence (`Tree.reasoned`) and never confirm a link.
    - **Recognition.** Each candidate a reasoned answer starts with, where the first-impression minds don't already give it, becomes an **inhibit** question to the first-impression roster: *does this symbol come directly after the run?* yes / no / can't tell. A candidate that is recognised when shown, though not produced unprompted, is evidence of a felt link reachable only by being pointed to. That distinction matters for signa, which always show the full sequence.
    - **First live check** [observed]. Given `🮂 🮁 🮀`, the reasoner looked up the surrounding code-point range and wrote a long descending run of chart neighbours. Given `ↂ ↇ ↈ` (the end of the Roman numerals), it answered "none". Reasoned candidates are expected to be chart-heavy, so recognition is the test that matters.
  - **Chart knowledge versus sequence knowledge.** The embedding spike's verifier found that the minds put the *alphabet* letter first wherever Unicode order and the alphabet disagree. The chart glyph shows up as runner-up for Claude and Gemini, never for Grok (`spikes/embedding-tendrils-2026-10-05/de-novo-feedback-1.md`, small n). So a ±1-codepoint link is not by itself a chart artefact.
  - **A clean marker of code-point arithmetic.** Some continuations name code points that are unassigned in Unicode 16, so they can never have been seen in text. Through c001 [measured, from `other_content` "unassigned" proposals, per 1,000 continuation answers]:

    | mind | rate |
    |---|---|
    | haiku45 (thinking 31000) | 35 |
    | gemini31pro | 21 |
    | gemini38flash | 15 |
    | sonnet55 | 9 |
    | grok46 | 8 |
    | opus55 | 0 |

    The flagship case is the Mayan numerals `𝋠 … 𝋳` (0–19). After `𝋱 𝋲 𝋳`, every family writes U+1D2F4 onward. These answers are kept as their own outcome, never as glyphs. The rate per mind and per thinking condition is a read-off of chart-following. *(Until c002, the pipeline ran on Unicode 14 data, so 3 such answers were in fact assigned characters (🯯 🩷 🩵). From then on, `run.py` requires Unicode 16+, and each plan and record carries its Unicode version.)*
  - **Recognition versus retrieval: the thinking budget is a probing factor.** Joseph: reasoning can be needed *"to discover the candidate sequences/branches/etc. that can be felt without much reasoning"*, which he called *"analogous to 'recognition vs retrieval'"*.
    - **How much the minds deliberate.** In c001, median thinking tokens per sheet ran from 0 (Gemini Flash) through ~500 (Sonnet) and ~900 (Grok) to ~2,400 (Gemini Pro) and ~5,100 (Haiku).
    - **An inherited budget.** Until 2026-10-05, the Claude judges inherited `MAX_THINKING_TOKENS=31000` from Joseph's shell, unrecorded. Budgets are now set per mind in `core/minds.json` and recorded in every ledger row.
    - **Thinking-off Haiku.** `haiku45nt` (budget 0) answers every sheet; `haiku45` (31000) is sampled as a second mind. On 102 items, thinking changed Haiku's first answer beyond its own retest noise (on–off agreement 0.69–0.74, against 0.83–0.88 within either condition), in both directions. It did not make Haiku more chart-bound. `spikes/thinking-felt-2026-10-05/` has the details.
    - **No off switch for Sonnet or Grok.** Sonnet's thinking isn't reached by the budget, and Grok's floor is `low`.
    - **What counts as felt.** A link is best evidenced as felt when it holds across conditions and families whose deliberation differs. Reasoned answers generate candidates; recognition-condition answers test them.

## 5. What gets asked next

This is Joseph's priority rule, restated on the tree:

> *"various minds start to find a sequence — call it a sequence of three glyphs. The priority is then to extend that sequence to the right and to the left as far as they will go while still spending time looking for other 'kernels' … square away the most obvious and stable (empirically) sequences."*
>
> *"15% of our effort was always 'hot' — exploring the space for more kernels … based on bumps from the original seed."*

- **Kernel.** A 3-glyph path that two or more minds agree on (a 2-glyph context with an agreed continuation), found from any kind of answer.
- **Squaring away** (85%). Each sequence's work is to:
  - push its ends outward with continue questions;
  - lengthen contexts until each position's k\* is found and its stability shown;
  - probe the branch points the tree exposes.

  Sequences are served most stable first.
- **Hot exploration** (15%). Fresh glyphs from the whole symbol space, weighted toward printable ASCII, then 2-byte, then 3- and 4-byte (Joseph, 2026-10-05). Exploration also favours **nodes that are still reaching out**: nodes with few settled edges get more tendrils. Settled nodes keep a floor of exploration, because creative sequences (`3E[|]3E[|]`) come from nodes that look settled.
- **Seeds** are tagged votes (§2a) and *contexts to query*. A seeded step is asked of the real minds when its sequence is served (tier 1), and its k\* is then found from short context upward like any other step.

## 6. Porting the triad era (concern 4)

Rounds r000–r012 ported **answers only**. Nothing derived is ported: no grown rows, fits, standings or stable counts, because each of those carries a rule of the old machinery. Every ported answer keeps all of its tags: round, sheet, position, sheet size, offered options (⟂ / tie / gap, forced or not), mind, family, prompt version, and the item's source as metadata. Concern 2 never reads the source.

| triad-era answer | ported as | not ported as, and why |
|---|---|---|
| what-comes-next: context (2–8 glyphs) → up to 3 proposals, best first, or "none" | continuation answers at that context node, with each proposal's rank; "none" as an end answer | — |
| triad: middle / only two / none / ties | short-context betweenness and orthogonality among the three glyphs (§2b) | **not edges.** A middle says `q` lies between `p` and `r`, not that `q` is adjacent to either |
| order: lines over a shown set, extras, none, ties, gaps | ordering and orthogonality constraints over the set (§2b) | **not edges.** A line orders a *subset*, so neighbours in a line need not be adjacent in any sequence |
| between: left run, GAP, right run → proposals or "none" | two-sided fill answers, their own kind | not continuations: the answer is conditioned on both sides |
| unparsed answers | recorded as an outcome with their reason | **not dropped silently.** The pilot found that failures cluster by glyph, so they are not missing at random |

**Checks before an answer enters the tree:**
- **Proposal content.** Each proposal must be one glyph, after NFC normalization. Words, fragments (`cir` was seen) and multi-glyph strings are kept as their own outcome and reported, never split into glyphs.
- **Selection.** Which contexts were asked, and how often, was steered by seeds, the old fit and the old planner, and the roster changed (glimmer early, second minds sampled). So agreement is always read as a *share* of the answers given at a node, per family, never as a raw count that rewards over-asked contexts.
- **Roster balance.** Families answered different volumes in different rounds, so per-family shares come before any pooling.
- **Out of scope.** The magnitude-era data in `../.archive/` asked a different question and is not ported.

The port writes a report: counts in and out by kind, everything excluded with its reason, and spot checks of ported nodes against the raw ledgers. That report is the audit trail.

## 6a. Machinery that carries over

The judge adapters, sheets, fate, parser and ledgers in `../harness/core` and `../harness/seq` are reference and copy source.

## 7. Open questions

- **Embeddings as tendrils.** Do a glyph's embedding neighbours predict confirmed edges better than its codepoint neighbours do? It's worth a fresh-agent spike that scores both against the stable sequences found so far. If they do, embeddings would choose what to probe. They would never be evidence. (Doubt: local models handle Unicode poorly.)
- **Agreement: soft, not a gate.** Agreement at a node is a quantity: the share of answers, and of families, giving the continuation. Priority (concern 3) uses it continuously, as a weight in the stochastic choice of what to ask. Nothing is filtered by it. Any "stable / not stable" label in a report is a read-off, and its cut-off is listed as a parameter chosen without evidence. (Joseph: *"I suspect it will be kind of a relative number or a soft threshold for the stochastic prioritization."*)
- **Reflection-symmetric cycles**, as in §3.

---

*Provenance: Joseph's turns on 2026-10-05 (quoted). The prior machinery and its incidents are in `../PLAN.md`, `../OBSERVATIONS.md` and the git log of `../harness/seq/`.*
