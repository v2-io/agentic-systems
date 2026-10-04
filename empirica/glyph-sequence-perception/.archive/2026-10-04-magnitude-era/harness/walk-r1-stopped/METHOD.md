# The stochastic walk: the method of 2026-08-25, as recorded, and how it is run here

*Assembled 2026-10-04 from primary sources only:*

- *Joseph's typed turns in the 08-25 session (transcript `60066910…jsonl`, read from `~/.claude.bak.2026-09-23/`);*
- *the pilot's own sampler code from that session;*
- *`pilot/pilot-record.md`;*
- *`pilot/DESIGN-scale-up.md`, including its addenda;*
- *`data/surveys-v1/RECONCILIATION-QUEUE.md`.*

*Nothing here comes from v1.0 or from a coordinator's account. The v1.0 runner's judge adapters, parser and fated-seed functions are reused as tools only (`harness/runner/`).*

## The method, in its sources' words

**Purpose.** Joseph, 08-25:

> *"Stochastically this should be a way of discovering sequences without *any prior information about the glyphs whatsoever*, if the area-filling / monte carlo walk is well-designed and if we don't inject assumptions like pearson correlation etc. that are layering our assumptions on what could otherwise be pure empirical results."*

**Elements**, each with its source:

| element | source |
|---|---|
| A "leave blank" / ⟂ option "if you don't perceive an ordering". | Joseph, 08-25 |
| "randomize the 'symbols you are choosing from' each time, and make sure anything that is stochastically in there left()right is also in a nearby one or even the same answer-sheet as right()left" | Joseph, 08-25 |
| A pool of known glyphs plus random dilution: walk1 used 188 + 90. Uniform random pairs at about 8 comparisons per glyph. Both orders on the same sheet, shuffled. Twelve independent judges, one sheet each. | pilot sampler, transcript line 577 |
| An edge exists only when both orders name the same glyph. ≈ ties are kept raw (≈ is not transitive). "No prior orderings, families, or expected values enter anywhere." | `harness/pilot-scripts/discover2.py` |
| Densification: "60% of pairs densify within the structured neighborhoods round 1 discovered (including 2-hop mixing so chains can splice), 25% structured-vs-anywhere-in-pool, 15% pure long tail". The long tail uses fixed codepoint ranges. | pilot, transcript lines 625 and 638 (walk2, walk4) |
| "discovery walks NEED the ⟂ option from the start" | pilot-record, walk3 |
| Graded felt distance (somewhat / much / vastly). | pilot-record, walk4 |
| Triads at the same 60/25/15 mixture. Judge 2p sees AB, BC, CA; judge 2p+1 sees BA, CB, AC. Option order permuted per judge. | pilot, transcript line 727; `walk5b-script.js` |
| PROTOCOL (final form): triads with reverse cycles split across two judges; presentations shuffled; glyph-echo + felt distance + ≈ + ⟂; option order permuted; mixture sampling; edges only where both judges agree across reverse presentations; chains as longest paths; cycles and disagreements reported, never patched. | pilot-record §PROTOCOL |
| The loop: walk → poset store → continuation agents propose rungs at the frontier → salting validates → accepted rungs re-enter the walk pool → candidate sequences go to gestalt validation → holistic candidates go to length-graded continuation → generator lattices are tracked as objects. Stop rule: loop until dry. | DESIGN §The loop |
| Must-fix list: ban ≈/⟂ from stimuli; an answer fallback for echo failures; option permutation per item; pinned models, recorded per call; the ledger. | DESIGN §Must fix |
| Addenda: fated randomness; a lineage label on every glyph; surveys are seeds, never data; no mechanism registry; sampling is structure-blind and graph-driven; Postgres 18 as the index. | DESIGN addenda; RECONCILIATION-QUEUE |

## How it is run here (`harness/walk/walk.py`)

Rounds follow the pilot's sequence.

| round | what | pilot analogue |
|---|---|---|
| `r1` | **Pool:** every glyph named by any record in all seven surveys, of every type (2,104), plus 1,007 long-tail glyphs drawn with the pilot's sampler at the pilot's ratio of 90 per 188. **Sampling:** uniform random pairs at ~8 per glyph, 12,444 pairs. **Presentation:** both orders on the same sheet, shuffled. | walk1, with ⟂ from the start |
| `r2` | Pairs: 60% within 2-hop structured neighbourhoods (structure = glyphs in any judge's consistent edge), 25% structured vs pool, 15% long tail. | walk2 / walk4 |
| `r3` | Triads at the same mixture, reverse cycles split across two independent instances of each judge. | walk5 / walk5b |
| then | The loop: frontier continuation → salting → re-entry → gestalt validation → generator lattices, until dry. | DESIGN §The loop |

**Panel:** the same sheets go to several LLM families. The question is inter-family intuition *from LLMs*, so each family's walk is reported separately and also in agreement with the others.

- Claude: Sonnet 5.5, Opus 5.5, Haiku 4.5;
- xAI: Grok 4.6;
- Google: Gemini 3.8 Flash, Gemini 3.1 Pro.

## Where this departs from the pilot, and why

| departure | reason |
|---|---|
| **40 presentations per sheet**, against ~185 in the pilot. | Long sheets lost answers for non-Claude judges in v1.0. A sheet that parses for fewer than 90% of its items is re-asked; its raw answer is kept. |
| **Judges are isolated CLI or API calls** (tools, MCP and instruction files stripped). The pilot's judges were Claude Code subagents carrying your global instructions. | One condition for every family. *This changes ⟂ use*: v1.0 measured about 1.6–1.85× more ⟂ for the same model in the subagent context. A context arm can be added if you want it. |
| **The pool keeps ASCII and every pilot glyph.** | Discovery uses the whole seed space. Held-out pools belong only to a later confirmation, if there is one. |
| **Option order is permuted per sheet**, against per judge in walk5b. Per item is not possible on a sheet, where the options are listed once. | — |
| **Small local models are not in the sheet rounds yet.** | They cannot answer 40-item JSON sheets reliably. They can join as single-presentation calls, at the cost of many calls per round. |
