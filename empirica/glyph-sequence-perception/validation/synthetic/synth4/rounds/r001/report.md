# Round r001 — fit report

Observations (triple-level, cumulative): 4288. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of chains and posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 4 | `⚀ ⚁ ⚂=⚃ ⚄ ⚅` | 6 | 1.00 | 0.81/0.97 | 0.65/0.97 | 0.65/0.90 |
| 3 | `▇ ▆ ▅ ⚁ ▄ ➺ ▃ ❖ ▂ ▁` | 10 | 0.67 | 0.73/0.89 | 0.65/0.97 | 0.50/0.65 |
| 1 | `⑤ ⑷ ⑸ ⑹` | 4 | 0.67 | 0.73/0.73 | 0.50/0.65 | 0.35/0.97 |
| 2 | `● ◕ ◑ ◔ ○` | 5 | 0.67 | 0.05/0.89 | 0.10/0.90 | 0.00/0.50 |
| 0 | `⑧ ⑦ ⑥ ⑤ ④ ③ ② ①` | 8 | 1.00 | 0.85/0.97 | 0.80/0.80 | 0.35/0.50 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.1 | 0.2 | 0.3 | 0.34 | 0.9 |
| synB | 0.15 | 0.4 | 0.3 | 0.5 | 0.9 |
| synC | 0.1 | 0.4 | 0.3 | 0.2 | 0.9 |
| synD | 0.4 | 0.2 | 0.2 | 0.65 | 0.9 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 20 | 0.33 | 1.00 |
| synB | 7 | 0.43 | 0.71 |
| synC | 7 | 0.29 | 0.86 |
| synD | 11 | 0.64 | 0.18 |

## Parse status this round

- synA|ok: 213
- synB|ok: 213
- synC|ok: 213
- synD|ok: 213
