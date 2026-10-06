# Round r001 — fit report

Observations (triple-level, cumulative): 3636. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of chains and posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 0 | `① ② ③ ④ ⑤ ⑥ ⑦ ⑧` | 8 | 1.00 | 0.85/0.97 | 0.65/0.97 | 0.65/0.97 |
| 2 | `⑤ ⑷ ⑸ ⑹` | 4 | 1.00 | 0.89/0.73 | 0.35/0.65 | 0.65/0.97 |
| 1 | `▁ ▂ ▃ ▄ ▅ ▆ ▇` | 7 | 0.67 | 0.78/0.90 | 0.65/0.97 | 0.50/0.50 |
| 3 | `⚀ ⚁ ⚂ ⚄ ⚅` | 5 | 1.00 | 0.00/0.85 | 0.00/0.97 | 0.00/0.50 |
| 4 | `⚀ ⚁ ⚂=⚃ ⚄ ⚅` | 6 | 1.00 | 0.81/0.00 | 0.65/0.00 | 0.50/0.20 |
| 5 | `○ ◔ ◑ ◕ ●` | 5 | 1.00 | 0.05/0.66 | 0.10/0.80 | 0.00/0.20 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.05 | 0.8 | 0.1 | 0.34 | 0.5 |
| synB | 0.15 | 0.6 | 0.2 | 0.5 | 0.5 |
| synC | 0.05 | 0.05 | 0.3 | 0.34 | 0.9 |
| synD | 0.4 | 0.2 | 0.2 | 0.65 | 0.1 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 19 | 0.32 | 0.89 |
| synB | 12 | 0.33 | 0.83 |
| synC | 7 | 0.33 | 0.86 |
| synD | 10 | 0.60 | 0.00 |

## Parse status this round

- synA|ok: 202
- synB|ok: 202
- synC|ok: 202
- synD|ok: 202
