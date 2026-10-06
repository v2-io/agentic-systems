# Round r001 — fit report

Observations (triple-level, cumulative): 3484. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of chains and posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 2 | `① ② ③ ④ ⑤ ⑥ ⑦ ⑧` | 8 | 0.33 | 0.78/0.90 | 0.65/0.90 | 0.90/0.90 |
| 4 | `⚅ ⚄ ⚂=⚃ ⚁ ⚀` | 6 | 0.67 | 0.78/0.90 | 0.65/0.90 | 0.65/0.65 |
| 0 | `▇ ▆ ▅ ▄ ▃ ▂ ▁` | 7 | 0.33 | 0.73/0.78 | 0.65/0.80 | 0.80/0.65 |
| 3 | `⑤ ⑷ ⑸ ⑹` | 4 | 0.33 | 0.78/0.78 | 0.65/0.65 | 0.35/0.90 |
| 1 | `● ◕ ◑ ◔ ○` | 5 | 0.67 | 0.07/0.62 | 0.03/0.97 | 0.00/0.03 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.1 | 0.4 | 0.3 | 0.34 | 0.7 |
| synB | 0.15 | 0.4 | 0.3 | 0.5 | 0.9 |
| synC | 0.1 | 0.4 | 0.3 | 0.5 | 0.7 |
| synD | 0.6 | 0.4 | 0.2 | 0.65 | 0.1 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 17 | 0.33 | 0.88 |
| synB | 6 | 0.33 | 1.00 |
| synC | 6 | 0.39 | 0.83 |
| synD | 9 | 0.63 | 0.33 |

## Parse status this round

- synA|ok: 197
- synB|ok: 197
- synC|ok: 197
- synD|ok: 197
