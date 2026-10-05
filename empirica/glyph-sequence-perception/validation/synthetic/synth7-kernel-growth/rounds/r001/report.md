# Round r001 — fit report

Observations (triple-level, cumulative): 13480. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of the cold-started chains (from seeds, not from the last fit) and their posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 1 | `▁ ▂ ▃ ▄ ▅ ▆ ▇` | 7 | 1.00 | 0.89/0.94 | 0.65/0.90 | 0.65/0.97 |
| 0 | `① ② ③ ④ ⑤ ⑥ ⑦ ⑧` | 8 | 1.00 | 0.89/0.89 | 0.50/0.97 | 0.90/0.65 |
| 4 | `○ ◔ ◑ ◕ ●` | 5 | 1.00 | 0.05/0.89 | 0.03/0.97 | 0.35/0.90 |
| 5 | `⚀ ⚁ ⚂ ⚄ ⚅` | 5 | 1.00 | 0.45/0.90 | 0.00/0.90 | 0.00/0.65 |
| 3 | `⑤ ⑷ ⑸ ⑹` | 4 | 0.00 | 0.89/0.28 | 0.50/0.35 | 0.90/0.20 |
| 2 | `⚀ ⚁ ⚃=⚂ ⚄ ⚅` | 6 | 1.00 | 0.89/0.50 | 0.65/0.50 | 0.65/0.50 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.15 | 0.6 | 0.1 | 0.5 | 0.5 |
| synB | 0.15 | 0.4 | 0.3 | 0.65 | 0.7 |
| synC | 0.15 | 0.8 | 0.1 | 0.65 | 0.9 |
| synD | 0.6 | 0.4 | 0.3 | 0.5 | 0.5 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 12 | 0.33 | 1.00 |
| synB | 5 | 0.40 | 0.80 |
| synC | 3 | 0.33 | 1.00 |
| synD | 6 | 0.67 | 0.33 |

## Parse status this round

- synA|ok: 299
- synB|ok: 299
- synC|ok: 299
- synD|ok: 299
