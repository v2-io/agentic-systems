# seeds/ — where seed ideas land

Every idea about where the stochastic queue should look goes here, as it comes up in analysis, hypothesizing or conversation. A seed **only raises the priority** of its glyphs and sets in the queue (`../../PLAN.md` §4, §7). It never excludes anything, never sets a reference order, and never enters a statistic.

The surveys in `../surveys-v1/` are already seeds. Their 1,235 records are ingested as-is, so nothing from them needs re-entering here.

## Format

One JSON object per line, in any `*.jsonl` file here. Group related seeds into one file named for the idea, e.g. `digit-dresses.jsonl`. Append to a file; never edit a line once written. To retract a seed, append a later line with `"retracts": "<id>"`.

| field | required | meaning |
|---|---|---|
| `id` | yes | `sha256("seed|" + file-stem + "|" + n)[:16]`, where n is the line's 0-based index in its file; or any unique string |
| `kind` | yes | `set` (look at these together; no order implied), `sequence` (a proposed order, **unoriented**: it and its reverse are the same), or `lattice` (a product of factors; every chain through it is a candidate) |
| `glyphs` | yes | the glyphs, as a string or a list. For `lattice`, every glyph in the product |
| `factors` | lattice only | `{factor_name: [values…]}`, plus `cells: {"<v1>|<v2>": glyph}` |
| `author` | yes | who proposed it (Joseph, an agent and its session, a survey) |
| `date` | yes | ISO date |
| `origin` | yes | where the idea came from, in a line or two: an analysis result, a conversation, a hunch |
| `bump` | no | a priority multiplier. Default 2.0; surveys use 1.5. It decays once the seed's glyphs reach the density target |
| `note` | no | anything else |

## Files

- `digit-dresses.jsonl`: the digit "dresses" (plain, superscript, subscript, circled, parenthesized, full stop, negative circled, dingbat circled sans and its negative form, double circled, fullwidth, comma, segmented, and five math styles) × values 1–9, as one lattice. Joseph's `①` vs `⑴` vs `❶` vs `🯱` question. Built by `digit_dresses.py`.
