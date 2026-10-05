# Round r003 — fit report

Observations (triple-level, cumulative): 9320. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of chains and posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 0 | `⑧ ⑦ ⑥ ⑤ ④ ③ ② ①` | 8 | 1.00 | 0.85/0.89 | 0.80/0.90 | 0.80/0.97 |
| 2 | `▇ ▆ ▅ ▄ ▃ ▂ ▁` | 7 | 1.00 | 0.78/0.85 | 0.65/0.97 | 0.65/0.90 |
| 3 | `⑵ ⑶ ⑤ ⑷ ⑸ ⑹` | 6 | 1.00 | 0.85/0.89 | 0.65/0.80 | 0.50/0.97 |
| 5 | `⚅ ⚄ ⚂ ⚁ ⚀` | 5 | 1.00 | 0.00/0.90 | 0.00/0.65 | 0.00/0.97 |
| 1 | `● ◕ ◑ ◔ ○` | 5 | 1.00 | 0.03/0.89 | 0.03/0.97 | 0.00/0.50 |
| 4 | `⚀ ⚁ ⚃=⚂ ⚄ ⚅` | 6 | 1.00 | 0.78/0.50 | 0.65/0.20 | 0.80/0.80 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.1 | 0.4 | 0.2 | 0.34 | 0.9 |
| synB | 0.15 | 0.4 | 0.2 | 0.65 | 0.9 |
| synC | 0.1 | 0.6 | 0.2 | 0.34 | 0.9 |
| synD | 0.6 | 0.4 | 0.2 | 0.5 | 0.9 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 34 | 0.36 | 0.91 |
| synB | 18 | 0.50 | 0.56 |
| synC | 14 | 0.31 | 0.93 |
| synD | 22 | 0.64 | 0.09 |

## Parse status this round

- synA|ok: 207
- synB|ok: 207
- synC|ok: 207
- synD|ok: 207
