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
3. **Priority: what to ask next.** It reads the tree and decides where effort goes: extension, k\*, branch points, cycle probes, hot exploration, seeds, and how settled each node is. It writes questions, never evidence. Seeds live entirely here.

The triad era mixed these concerns:
- seeds supplied the glyphs that sequences were tested with;
- the fit's guesses steered what was asked within sequences;
- the growth rules carried priority judgments.

Each mix-up produced an incident (see `../OBSERVATIONS.md` and the seam note in `../PLAN.md`).

## 3. Definitions

**Shortest sufficient context, k\*.** For a glyph `x` that follows a run `… u v w` along some path, k\* is the length of the shortest suffix of that run (`w`, `v w`, `u v w`, …) at which minds name `x` as the continuation.

**Stability** (per position). An edge is **stable** when two things hold:
- the minds agree on it at k\*;
- the prediction stays put when the context is lengthened backward along the same path.

A long k\* is not a weakness; it makes the edge specific. The spinner's `-` may need `\ | /` before it. The failure mode is the opposite: a prediction that flips when more context is shown (`7 8 9 → 🔟`, but `7 8 9 8 → 7`). Flips are where branches live.
A node's **restfulness** is how settled its continuation already is at short context. `3` after `1 2` is restful.

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
- **Lengthening contexts.** To find k\* for an edge, ask its context at increasing lengths along the path, starting short.
- **No spoiling.** A context never shows what the question is testing. For a suspected cycle, show only enough of the period's end that a repeat would be the mind's own. For an extension, never include glyphs from beyond the end.
- **Triads and order sets** are cheap consistency checks. A sequence implies betweenness for each of its triples, and an order for each of its windows. A triad answer is also an unconditioned hint that a 3-glyph path exists, which makes it a cheap way to find **kernels** during exploration. They do not create edges.
- **Sheets** keep everything the pilot and rounds r000–r012 established: 1–5 presentations per call, fated randomization, recorded positions, and isolated judge adapters.

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
- **Seeds** are proposed *contexts to query*, never edges. A seed's written order says which contexts to ask first; each of its edges is then checked from short context upward. Their only standing is priority.

## 6. What carries over from rounds r000–r012

- **Continuation evidence:** what-comes-next answers and their 3–8-glyph contexts (5,443 answers through r011). They drop straight into the tree, as the first glyph of a continuation.
- **Consistency evidence:** triad answers (17,928) and order answers (6,224), as checks and as kernel hints.
- **Machinery:** the judge adapters, sheets, fate, parser and ledgers in `../harness/core` and `../harness/seq`.

## 7. Open questions

- **Embeddings as tendrils.** Do a glyph's embedding neighbours predict confirmed edges better than its codepoint neighbours do? It's worth a fresh-agent spike that scores both against the stable sequences found so far. If they do, embeddings would choose what to probe. They would never be evidence. (Doubt: local models handle Unicode poorly.)
- **Agreement: soft, not a gate.** Agreement at a node is a quantity: the share of answers, and of families, giving the continuation. Priority (concern 3) uses it continuously, as a weight in the stochastic choice of what to ask. Nothing is filtered by it. Any "stable / not stable" label in a report is a read-off, and its cut-off is listed as a parameter chosen without evidence. (Joseph: *"I suspect it will be kind of a relative number or a soft threshold for the stochastic prioritization."*)
- **Reflection-symmetric cycles**, as in §3.

---

*Provenance: Joseph's turns on 2026-10-05 (quoted). The prior machinery and its incidents are in `../PLAN.md`, `../OBSERVATIONS.md` and the git log of `../harness/seq/`.*
