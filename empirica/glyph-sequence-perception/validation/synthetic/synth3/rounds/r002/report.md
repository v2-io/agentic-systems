# Round r002 — fit report

Observations (triple-level, cumulative): 6672. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of chains and posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 2 | `▁ ▂ ▃ ▄ ▅ ▆ ▇` | 7 | 0.67 | 0.85/0.85 | 0.65/0.90 | 0.80/0.90 |
| 3 | `① ② ⚅ ③ ④ ⚄ ⑤=⚂=⚃ ⚁ ⚀ ⑥ ⑦ ⑧` | 14 | 0.67 | 0.89/0.97 | 0.65/0.80 | 0.65/0.80 |
| 1 | `⑹ ⑸ ⑷ ⑤` | 4 | 0.67 | 0.89/0.81 | 0.50/0.65 | 0.50/0.97 |
| 0 | `● ◕ ◑ ◔ ○` | 5 | 1.00 | 0.10/0.73 | 0.10/0.97 | 0.00/0.65 |
| 4 | `⑵ ⑶ ⑤ ⑷` | 4 | 1.00 | 0.90/0.00 | 0.35/0.00 | 0.90/0.00 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.15 | 0.6 | 0.2 | 0.34 | 0.7 |
| synB | 0.25 | 0.6 | 0.3 | 0.5 | 0.9 |
| synC | 0.1 | 0.6 | 0.3 | 0.5 | 0.7 |
| synD | 0.6 | 0.4 | 0.2 | 0.5 | 0.1 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 22 | 0.33 | 0.91 |
| synB | 9 | 0.33 | 1.00 |
| synC | 10 | 0.37 | 0.90 |
| synD | 13 | 0.59 | 0.31 |

## Parse status this round

- synA|ok: 183
- synB|ok: 183
- synC|ok: 183
- synD|ok: 183
