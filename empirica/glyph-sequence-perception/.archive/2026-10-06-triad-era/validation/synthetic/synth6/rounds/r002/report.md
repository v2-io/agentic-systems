# Round r002 — fit report

Observations (triple-level, cumulative): 6936. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of chains and posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 0 | `① ② ③ ④ ⑤ ⑥ ⑦ ⑧` | 8 | 0.67 | 0.85/0.94 | 0.65/0.97 | 0.80/0.90 |
| 2 | `▁ ▂ ▃ ▄ ▅ ▆ ▇` | 7 | 0.67 | 0.89/0.94 | 0.65/0.97 | 0.65/0.90 |
| 3 | `⑵ ⑶ ⑤ ⑷ ⑸ ⑹` | 6 | 0.67 | 0.89/0.70 | 0.50/0.80 | 0.65/0.97 |
| 1 | `⚀ ⚁ ⚂ ⚄ ⚅` | 5 | 1.00 | 0.00/0.89 | 0.00/0.97 | 0.00/0.65 |
| 4 | `⚀ ⚁ ⚂=⚃ ⚄ ⚅` | 6 | 1.00 | 0.78/0.10 | 0.65/0.10 | 0.65/0.00 |
| 5 | `○ ◔ ◑ ◕ ●` | 5 | 1.00 | 0.05/0.78 | 0.10/0.65 | 0.00/0.65 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.1 | 0.8 | 0.1 | 0.5 | 0.7 |
| synB | 0.1 | 0.4 | 0.3 | 0.65 | 0.5 |
| synC | 0.1 | 0.6 | 0.2 | 0.34 | 0.9 |
| synD | 0.6 | 0.4 | 0.2 | 0.65 | 0.1 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 25 | 0.32 | 0.92 |
| synB | 16 | 0.35 | 0.81 |
| synC | 9 | 0.33 | 0.89 |
| synD | 13 | 0.54 | 0.00 |

## Parse status this round

- synA|ok: 177
- synB|ok: 177
- synC|ok: 177
- synD|ok: 177
