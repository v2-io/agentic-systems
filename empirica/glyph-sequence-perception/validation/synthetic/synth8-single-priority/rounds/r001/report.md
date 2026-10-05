# Round r001 — fit report

Observations (triple-level, cumulative): 3324. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of the cold-started chains (from seeds, not from the last fit) and their posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 2 | `⑧ ⑦ ⑥ ⑤ ④ ③ ② ①` | 8 | 1.00 | 0.85/0.89 | 0.50/0.80 | 0.90/0.97 |
| 0 | `▁ ▂ ▃ ▄ ▅ ▆ ▇` | 7 | 1.00 | 0.81/0.89 | 0.65/0.65 | 0.80/0.00 |
| 1 | `⚀ ⚁ ⚃=⚂ ⚄ ⚅` | 6 | 1.00 | 0.78/0.78 | 0.50/0.50 | 0.97/0.97 |
| 3 | `⑤ ⑷ ⑸ ⑹` | 4 | 1.00 | 0.80/0.00 | 0.50/0.00 | 0.80/0.10 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.15 | 0.8 | 0.1 | 0.34 | 0.1 |
| synB | 0.1 | 0.6 | 0.2 | 0.65 | 0.1 |
| synC | 0.05 | 0.8 | 0.2 | 0.34 | 0.1 |
| synD | 0.6 | 0.4 | 0.1 | 0.65 | 0.1 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 10 | 0.33 | 0.90 |
| synB | 4 | 0.33 | 1.00 |
| synC | 6 | 0.33 | 0.67 |
| synD | 5 | 0.60 | 0.20 |

## Parse status this round

- synA|ok: 300
- synB|ok: 300
- synC|ok: 300
- synD|ok: 300
