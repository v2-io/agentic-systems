# Naming Alias Clusters (`codex-2`)

This is a pre-aggregation note for `msc/naming/naming-votes/`. The goal is to collapse near-duplicate rename proposals into concept clusters before any tallying or synthesis.

This note does not pick winners. It identifies where multiple vote rows are really talking about the same underlying naming issue.

## Vote File Shorthand

- `codex-1`
- `codex-2`
- `opus-1m`
- `opus-4-7`
- `sonnet-4-6`
- `haiku-4-5`
- `gemini-1`
- `gemini-2`
- `agent1`

## Strong Consensus On The Underlying Issue

| Cluster | Variants seen in votes | Support observed | Aggregation read |
|---|---|---|---|
| Project-level `ASF` cleanup | `Agentic Systems Framework (ASF)` -> `Agentic Systems` | `codex-1`, `codex-2` | Treat as a straightforward live-surface cleanup cluster. Little evidence anyone wants to preserve `ASF`. |
| Software framing | `"richest operationalization domain"` / `"best operationalization domain"` -> `calibration laboratory` | `codex-1`, `codex-2`, `opus-1m`, `opus-4-7`, `sonnet-4-6` | Treat as consensus canonicalization, not an open contest. The real question is where to standardize the short form. |
| `act-agent` stale-slug problem | `#developer-as-act-agent`, `#ai-agent-as-act-agent` both flagged as stale | `codex-1`, `codex-2`, `opus-1m`, `agent1` | Consensus exists on the problem. The only open question is the landing slug family. |

## Split Clusters Requiring Real Judgment

| Cluster | Variants seen in votes | Support observed | Aggregation read |
|---|---|---|---|
| `#developer-as-act-agent` destination | `#developer-as-aad-agent`; `#developer-as-adaptive-agent`; `#developer-agent-mapping` | `codex-1`, `codex-2` support the `aad-agent` family; `opus-1m`, `agent1` support the `adaptive-agent` family; `agent1` also floats `developer-agent-mapping` weakly | Aggregate this as one rename cluster with a genuine philosophical split: framework-aligned slug vs framework-name-free slug. |
| `#ai-agent-as-act-agent` destination | `#ai-agent-as-aad-agent`; `#ai-agent-as-adaptive-agent` | `codex-1`, `codex-2` support the `aad-agent` family; `opus-1m`, `agent1` support the `adaptive-agent` family | Same split as the developer segment. These two should be decided together, not independently. |
| `#additive-coordinate-forcing` | `#forced-coordinates`; `#coordinate-forcing`; `#uniqueness-coordinate-forcing`; rejected side branch `#cauchy-coordinates` / `#axiom-forcing` | `codex-1`, `gemini-1`, `opus-1m`, `opus-4-7` lean toward the broader forcing family; `codex-2`, `haiku-4-5`, `opus-4-7`, `sonnet-4-6` give some support to `uniqueness-coordinate-forcing`; `sonnet-4-6` strongly favors `coordinate-forcing`; `agent1` weakly prefers `cauchy-coordinates` | Aggregate by underlying complaint first: the current title overstates additivity relative to the broader forcing/uniqueness discipline. Then compare destinations inside that family. Do not treat `forced-coordinates`, `coordinate-forcing`, and `uniqueness-coordinate-forcing` as unrelated proposals. |
| `#strategic-composition` | keep current; `#equilibrium-composition`; rejected `#game-theoretic-composition` | `codex-1`, `codex-2`, `opus-1m`, `opus-4-7`, `agent1` support `equilibrium-composition`; `haiku-4-5` strongly keeps current; `sonnet-4-6` is split/ambivalent; several files explicitly reject `game-theoretic-composition` | The live split is really keep-vs-`equilibrium-composition`. `game-theoretic-composition` is mostly a rejected foil, not a serious finalist. |
| `#interaction-channel-classification` | keep current; `#signal-reception-regimes`; `#recipient-regime-classification`; `#interaction-regimes` | `codex-1`, `codex-2` support `signal-reception-regimes`; `opus-4-7`, `sonnet-4-6` support `recipient-regime-classification`; `gemini-2` offers `interaction-regimes`; `haiku-4-5` and `sonnet-4-6` allow keeping current | Treat these as one cluster about foregrounding recipient-side regimes rather than bland taxonomy language. The variants are closer than they first appear. |
| `#m-preservation` | `#model-preservation`; `#epistemic-externalization` | `codex-1`, `codex-2` support `model-preservation`; `gemini-1` supports `epistemic-externalization` | Aggregate as one "replace symbolic slug with English" cluster. The real semantic choice is effect (`preservation`) vs mechanism (`externalization`). |
| `#section-ii-survival` | `#section-ii-carryover-map`; `#section-ii carryover classification` | `codex-1`, `codex-2` | Low-volume cluster, but both proposals point in the same direction: move away from survival language toward carryover language. |

## Mostly-Keep Clusters

| Cluster | Variants seen in votes | Support observed | Aggregation read |
|---|---|---|---|
| `#approximation-tiering` | keep current; `#approximation-ladders`; `#tiered-approximation` | `haiku-4-5`, `sonnet-4-6`, `opus-4-7` mostly keep; `codex-1`, `codex-2` offer weaker alternatives | Treat as mostly keep unless later synthesis strongly values shorter spoken phrasing. |
| `#agent-identity` | keep current; `#trajectory-identity`; `#causal-identity` | `opus-4-7`, `haiku-4-5` strongly keep; `codex-2` and `gemini-2` offer narrower alternatives | Aggregate as "current name broadly accepted; rename proposals are scope-tightening refinements." |
| `#agent-spectrum` | keep current; `#agency-spectrum` | `opus-4-7`, `haiku-4-5` keep; `codex-2` offers a weak alternative | Mostly keep. |
| `#shared-intent` | keep current; `#compressed-purpose` | `codex-1`, `codex-2`, `haiku-4-5` strongly keep; `gemini-2` offers one alternative | Strong keep cluster. |
| `#communication-gain` | keep current; `Trust gain` | `codex-1`, `codex-2`, `haiku-4-5` keep; `gemini-1` offers an alternative | Strong keep cluster. |

## Practical Aggregation Heuristic

When consolidating the vote sheets, the useful unit is not the literal string but the underlying complaint or ambition:

1. `stale acronym / stale rename residue`
2. `scope-honesty correction`
3. `recipient-side regime emphasis`
4. `replace symbol-first slug with English`
5. `keep current name; canonicalize short prose form`

Using that lens:

- `forced-coordinates`, `coordinate-forcing`, and `uniqueness-coordinate-forcing` belong in one family.
- `signal-reception-regimes`, `recipient-regime-classification`, and `interaction-regimes` belong in one family.
- `developer-as-aad-agent` and `developer-as-adaptive-agent` should be compared as two landings for one shared rename impulse, not counted as independent objections to the current slug.

## Most Decision-Relevant Open Split

The only cluster that looks both operationally urgent and substantively split is the `act-agent` destination family:

- `aad-agent` matches current visible titles and keeps the slugs aligned with the AAD umbrella.
- `adaptive-agent` avoids embedding the framework name in slugs and is more robust to future top-level renames.

Everything else can be aggregated more mechanically than that.
