# Round r002 — fit report

Observations (triple-level, cumulative): 6880. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of chains and posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 0 | `⑧ ⑦ ⑥ ⑤ ④ ③ ② ①` | 8 | 0.67 | 0.89/0.97 | 0.80/0.80 | 0.65/0.97 |
| 2 | `▇ ▆ ▅ ▄ ▃ ▂ ▁` | 7 | 0.33 | 0.78/0.85 | 0.65/0.97 | 0.65/0.80 |
| 3 | `⑤=⑶ ⑷ ⑸ ⑹ ⑵` | 6 | 1.00 | 0.85/0.73 | 0.65/0.65 | 0.65/0.97 |
| 4 | `⚀ ⚁ ⚂=⚃ ⚄ ⚅` | 6 | 1.00 | 0.78/0.90 | 0.65/0.65 | 0.65/0.90 |
| 1 | `● ◕ ◑ ◔ ○` | 5 | 1.00 | 0.07/0.94 | 0.03/0.97 | 0.00/0.50 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.1 | 0.6 | 0.2 | 0.34 | 0.9 |
| synB | 0.15 | 0.6 | 0.2 | 0.65 | 0.9 |
| synC | 0.1 | 0.6 | 0.2 | 0.34 | 0.7 |
| synD | 0.6 | 0.4 | 0.2 | 0.65 | 0.9 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 27 | 0.37 | 0.89 |
| synB | 13 | 0.46 | 0.62 |
| synC | 11 | 0.30 | 0.91 |
| synD | 18 | 0.57 | 0.11 |

## Parse status this round

- synA|ok: 193
- synB|ok: 193
- synC|ok: 193
- synD|ok: 193
